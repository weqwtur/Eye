from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxx4DG71/" 
VIDEO_ID = "BAACAgIAAxkBAAICY2oVEY0oyy-FKUoukUW6Vegnjt22AAKYkgACxbmoSNUPUdmkzbWqOwQ" 


@router.message(Command("media5"))
async def media5_command(message: types.Message):
    await media5_start(message)


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
