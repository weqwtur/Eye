from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuPWBAV/" 
VIDEO_ID = "BAACAgIAAxkBAAOgahPQFkXt0HCUKZG14JbMp_P-yaIAAnGSAALFuaBIClqMvFu6jUU7BA" 


@router.message(Command("media4"))
async def media4_command(message: types.Message):
    await media4_start(message)


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
