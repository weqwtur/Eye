from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxx4DG71/" 
VIDEO_ID = "BAACAgIAAxkBAAICY2oVEY0oyy-FKUoukUW6Vegnjt22AAKYkgACxbmoSNUPUdmkzbWqOwQ" 


async def media5_start(message: types.Message):
    kb = InlineKeyboardBuilder()


async def media5_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
