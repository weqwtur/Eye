from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxHkJDsq/" 
VIDEO_ID = "BAACAgIAAxkBAAPKahPnaKrPTXf2UXC11V_Wjpf1VyAAAvySAALFuaBIsD2XkZulew87BA" 


async def media8_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
