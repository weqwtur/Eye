import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from database import engine
from models import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher(storage=MemoryStorage())

from commands.start import router as start_router
from media_id import router as media_id_router

from commands.menu import router as menu_router, main_menu_kb, other_menu_kb, back_kb
from commands.top.top import router as top_router
from commands.media.media import router as media_menu_router
from commands.facts import router as facts_router
from commands.github import router as github_router

from commands.media.media1 import router as media1_router
from commands.media.media2 import router as media2_router
from commands.media.media3 import router as media3_router
from commands.media.media4 import router as media4_router
from commands.media.media5 import router as media5_router
from commands.media.media6 import router as media6_router
from commands.media.media7 import router as media7_router
from commands.media.media8 import router as media8_router
from commands.media.media9 import router as media9_router

from commands.braille import router as maritime_router
from commands.report import router as report_router


dp.include_router(start_router)
dp.include_router(report_router)

dp.include_router(media_id_router)

dp.include_router(menu_router)
dp.include_router(top_router)
dp.include_router(media_menu_router)
dp.include_router(facts_router)
dp.include_router(github_router)

dp.include_router(media1_router)
dp.include_router(media2_router)
dp.include_router(media3_router)
dp.include_router(media4_router)
dp.include_router(media5_router)
dp.include_router(media6_router)
dp.include_router(media7_router)
dp.include_router(media8_router)
dp.include_router(media9_router)

dp.include_router(maritime_router)


async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ The database is initialized")


async def main():
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

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped")
