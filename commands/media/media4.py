from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuPWBAV/" 
VIDEO_ID = "BAACAgIAAxkBAAOgahPQFkXt0HCUKZG14JbMp_P-yaIAAnGSAALFuaBIClqMvFu6jUU7BA" 


async def media4_start(message: types.Message):
    kb = InlineKeyboardBuilder()


async def media4_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
