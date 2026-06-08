from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxu5egng/" 
VIDEO_ID = "BAACAgIAAxkBAAOeahPPURZv3xHdIdK8niUdOTAGS_oAAmuSAALFuaBIXIhc4qhJVPg7BA" 


async def media3_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
