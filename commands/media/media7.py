from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxHhavh1/" 
VIDEO_ID = "BAACAgIAAxkBAAPIahPm_lCYp8Lxr6Mo_RTur8dehaAAAviSAALFuaBIvJD0UJCJn6o7BA" 


@router.message(Command("media7"))
async def media7_command(message: types.Message):
    await media7_start(message)


async def media7_start(message: types.Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=" ",
        url=TT_LINK
    )

    await message.answer_video(
        video=VIDEO_ID,
        reply_markup=kb.as_markup()
    )
