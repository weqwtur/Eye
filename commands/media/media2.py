from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuP1tjt/" 
VIDEO_ID = "BAACAgIAAxkBAAOYahPNKl8PTF6LQNYaxvM5I-bgohAAAmGSAALFuaBILU7OlNVrCeM7BA" 


@router.message(Command("media2"))
async def media2_command(message: types.Message):
    await media2_start(message)


async def media2_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
