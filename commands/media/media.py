import logging
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command("media"))
async def media_menu(message: types.Message):
    logger.info("📁 /media command received!")
    
    kb = InlineKeyboardBuilder()

    for i in range(1, 10):
        kb.button(
            text=f"{i}",
            callback_data=f"open_media:{i}"
        )

    kb.adjust(3, 3, 3)

    await message.answer(
        "📁 Choose media:",
        reply_markup=kb.as_markup()
    )
    
    logger.info("✅ /media reply sent")


@router.callback_query(F.data.startswith("open_media:"))
async def open_media(callback: types.CallbackQuery):
    media_id = int(callback.data.split(":")[1])

    if media_id == 1:
        from commands.media.media1 import media1_start
        return await media1_start(callback.message)

    if media_id == 2:
        from commands.media.media2 import media2_start
        return await media2_start(callback.message)

    if media_id == 3:
        from commands.media.media3 import media3_start
        return await media3_start(callback.message)
    
    if media_id == 4:
        from commands.media.media4 import media4_start
        return await media4_start(callback.message)
    
    if media_id == 5:
        from commands.media.media5 import media5_start
        return await media5_start(callback.message)
    
    if media_id == 6:
        from commands.media.media6 import media6_start
        return await media6_start(callback.message)
    
    if media_id == 7:
        from commands.media.media7 import media7_start
        return await media7_start(callback.message)
    
    if media_id == 8:
        from commands.media.media8 import media8_start
        return await media8_start(callback.message)
    
    if media_id == 9:
        from commands.media.media9 import media9_start
        return await media9_start(callback.message)

    await callback.answer("This media is not added yet")
