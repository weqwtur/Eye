import os
import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from aiohttp import web
from aiohttp.web import Application

from eye_bot.core.database import engine
from eye_bot.core.models import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)
DISABLE_TELEGRAM = os.getenv("DISABLE_TELEGRAM") in ("1", "true", "True")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher(storage=MemoryStorage())

from eye_bot.handlers.start import router as start_router
from eye_bot.handlers.media_id import router as media_id_router
from eye_bot.handlers.menu import router as menu_router
from eye_bot.handlers.top import router as top_router
from eye_bot.handlers.media import router as media_menu_router
from eye_bot.handlers.facts import router as facts_router
from eye_bot.handlers.github import router as github_router
from eye_bot.handlers.diseases import router as diseases_router
from eye_bot.handlers.ciphers import router as ciphers_router
from eye_bot.handlers.report import router as report_router
from eye_bot.handlers.media.router import router as media_router_subrouter

dp.include_router(start_router)
dp.include_router(report_router)
dp.include_router(media_id_router)
dp.include_router(menu_router)
dp.include_router(top_router)
dp.include_router(media_menu_router)
dp.include_router(facts_router)
dp.include_router(github_router)
dp.include_router(diseases_router)
dp.include_router(ciphers_router)

BASE_DIR = Path(__file__).parent.parent
# Prefer package static directory (eye_bot/static), fall back to project-level static
PACKAGE_STATIC = Path(__file__).parent / "static"

async def serve_static(request):
    filename = request.match_info.get('filename', '')
    # prefer package static if available (this repo places files under eye_bot/static/games)
    if (PACKAGE_STATIC / "games").exists():
        static_root = PACKAGE_STATIC / "games"
    else:
        static_root = PACKAGE_STATIC if PACKAGE_STATIC.exists() else (BASE_DIR / "static")
    # Prevent path traversal: resolve and ensure target is under static_root
    target = (static_root / filename).resolve()
    try:
        static_root_resolved = static_root.resolve()
    except Exception:
        static_root_resolved = static_root

    if static_root_resolved != target and static_root_resolved not in target.parents:
        logger.warning(f"Forbidden static access attempt: {target}")
        return web.Response(status=403, text="Forbidden")

    # If directory requested, serve its index.html
    if target.is_dir():
        target = target / "index.html"

    if target.exists() and target.is_file():
        logger.info(f"✅ Served static file: {target}")
        return web.FileResponse(target)

    logger.warning(f"❌ File not found: {target}")
    return web.Response(status=404, text=f"File not found: {filename}")


async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Database initialized")


async def flush_pending_updates():
    logger.info("🧹 Flushing pending updates...")
    try:
        updates = await bot.get_updates(offset=-1, timeout=0)
        if updates:
            await bot.get_updates(offset=updates[-1].update_id + 1, timeout=0)
    except Exception as e:
        # Don't fail startup on transient Telegram errors (e.g., another getUpdates running)
        logger.warning(f"Flush error (ignored): {e}")


async def main():
    if not DISABLE_TELEGRAM and ADMIN_ID == 0:
        raise RuntimeError("ADMIN_ID environment variable must be set when Telegram is enabled")

    dp.startup.register(on_startup)

    app = Application()
    app.router.add_get('/games/{filename:.*}', serve_static)

    async def index_redirect(request):
        return web.HTTPFound('/games/hit-the-eye/')
    app.router.add_get('/', index_redirect)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()

    logger.info("🌐 Web server started on port 8080")
    logger.info("🎮 Mini App: https://eye-production-853c.up.railway.app/games/hit-the-eye/")

    # If Telegram integration is disabled (local testing), skip polling.
    if not DISABLE_TELEGRAM:
        await flush_pending_updates()
        await dp.start_polling(bot)
    else:
        logger.info("ℹ️ Telegram disabled: running web server only (DISABLE_TELEGRAM=1)")
        # keep the process alive so the web server stays up for testing
        stop_event = asyncio.Event()
        try:
            await stop_event.wait()
        except asyncio.CancelledError:
            pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped")
    except Exception as e:
        logger.error(f"Critical error: {e}")