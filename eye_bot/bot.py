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

async def serve_static(request):
    filename = request.match_info['filename']
    file_path = BASE_DIR / "static" / filename
    if file_path.exists() and file_path.is_file():
        return web.FileResponse(file_path)
    logger.warning(f"❌ File not found: {file_path}")
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
        logger.error(f"Flush error: {e}")


async def main():
    if ADMIN_ID == 0:
        raise RuntimeError("ADMIN_ID environment variable must be set")

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

    await flush_pending_updates()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped")
    except Exception as e:
        logger.error(f"Critical error: {e}")