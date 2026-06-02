from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuPkR1u/" 
VIDEO_ID = "BAACAgIAAxkBAAOpahPRq7BOXO6z8bkbK_Wyun9FP1UAAnmSAALFuaBIGeAHoMcBIg87BA" 


@router.message(Command("media6"))
async def media6_command(message: types.Message):
    await media6_start(message)


async def media6_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
