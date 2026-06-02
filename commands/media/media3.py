from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxu5egng/" 
VIDEO_ID = "BAACAgIAAxkBAAOeahPPURZv3xHdIdK8niUdOTAGS_oAAmuSAALFuaBIXIhc4qhJVPg7BA" 


@router.message(Command("media3"))
async def media3_command(message: types.Message):
    await media3_start(message)


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
