import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

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

from eye_bot.handlers.media.router import router as media_router_subrouter

from eye_bot.handlers.ciphers import router as ciphers_router
from eye_bot.handlers.report import router as report_router


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


async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ The database is initialized")


async def flush_pending_updates() -> None:
    logger.info("🧹 Flushing pending updates before polling")
    updates = await bot.get_updates(offset=-1, timeout=0)
    if updates:
        last_update_id = updates[-1].update_id
        await bot.get_updates(offset=last_update_id + 1, timeout=0)


async def main():
    if ADMIN_ID == 0:
        raise RuntimeError(
            "ADMIN_ID environment variable must be set and non-zero before starting the bot."
        )

    dp.startup.register(on_startup)

    logger.info("=" * 50)
    logger.info(f"📍 ROUTERS REGISTERED: {len(dp.sub_routers)}")
    logger.info("=" * 50)

    for i, router in enumerate(dp.sub_routers, 1):
        message_handlers = len(router.message.handlers) if hasattr(router.message, 'handlers') else 0
        callback_handlers = len(router.callback_query.handlers) if hasattr(router.callback_query, 'handlers') else 0
        logger.info(f"   [{i}] Router - Message: {message_handlers}, Callback: {callback_handlers}")

    logger.info("=" * 50)
    logger.info("🚀 BOT STARTED - READY FOR COMMANDS")
    logger.info("=" * 50)

    await flush_pending_updates()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped")
