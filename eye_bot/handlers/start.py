from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import os

from eye_bot.core.database import SessionLocal
from eye_bot.core.models import UserClicks
from sqlalchemy import select

router = Router()

GIF_ID = os.getenv("GIF_ID")


@router.message(Command("start"), F.chat.type == "private")
async def start(message: types.Message):
    user_id = message.from_user.id

    async with SessionLocal() as session:
        result = await session.execute(
            select(UserClicks).where(UserClicks.user_id == user_id)
        )
        user = result.scalar()
        clicks = user.clicks if user else 0

    gif_msg = await message.answer_animation(animation=GIF_ID)
    await asyncio.sleep(0.05)

    counter_msg = await message.answer(str(clicks))

    kb = InlineKeyboardBuilder()
    kb.button(
        text=" ",
        icon_custom_emoji_id="6037397706505195857",
        callback_data=f"click:{counter_msg.message_id}"
    )

    await gif_msg.edit_reply_markup(reply_markup=kb.as_markup())


@router.callback_query(F.data.startswith("click:"), F.message.chat.type == "private")
async def click_handler(callback: types.CallbackQuery):
    _, counter_msg_id = callback.data.split(":")
    counter_msg_id = int(counter_msg_id)

    user_id = callback.from_user.id

    async with SessionLocal() as session:
        result = await session.execute(
            select(UserClicks).where(UserClicks.user_id == user_id)
        )
        user = result.scalar()

        if not user:
            user = UserClicks(user_id=user_id, clicks=0)
            session.add(user)

        user.clicks += 1
        await session.commit()

        new_value = user.clicks

    await callback.bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=counter_msg_id,
        text=str(new_value)
    )

    await callback.answer("👁️")
