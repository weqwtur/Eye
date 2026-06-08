from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuPkR1u/" 
VIDEO_ID = "BAACAgIAAxkBAAOpahPRq7BOXO6z8bkbK_Wyun9FP1UAAnmSAALFuaBIGeAHoMcBIg87BA" 


async def media6_start(message: types.Message):
    kb = InlineKeyboardBuilder()


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
