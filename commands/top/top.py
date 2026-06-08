from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import select, desc
import logging

from database import SessionLocal
from models import UserClicks
from commands.top.player_render import render_player_html

router = Router()
logger = logging.getLogger(__name__)

stats_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="eyes")],
    ],
    resize_keyboard=True
)

async def render_top():
    try:
        async with SessionLocal() as session:
            result = await session.execute(
                select(UserClicks).order_by(desc(UserClicks.clicks)).limit(10)
)
            rows = result.scalars().all()

        if not rows:
            return "👁️"

        lines = []
        for i, row in enumerate(rows, start=1):
            player_html = render_player_html(row.user_id)
            lines.append(f"{i}. {player_html} - {row.clicks}")

        return "Top eyes:\n\n" + "\n".join(lines)
    
    except Exception as e:
        logger.error(f"Error in render_top: {e}")
        return "❌ Error loading the top"


@router.message(Command("eyes"))
async def cmd_top(message: types.Message):
    text = await render_top()

    kb = InlineKeyboardBuilder()
    kb.button(
        text=" ",
        icon_custom_emoji_id="5346269127059196142",
        callback_data="refresh_eyes"
    )
    kb.row(types.InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back"))

    await message.answer(text, reply_markup=kb.as_markup())


async def show_top_in_menu(message: types.Message):
    """Called from menu - edits the existing message"""
    text = await render_top()

    kb = InlineKeyboardBuilder()
    kb.button(
            text=" ",
            icon_custom_emoji_id="5346269127059196142",
            callback_data="refresh_eyes"
        )
    kb.row(types.InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back"))

    await message.edit_text(text, reply_markup=kb.as_markup())


@router.callback_query(F.data == "refresh_eyes")
async def refresh_eyes(callback: types.CallbackQuery):
    
    await callback.answer("Updating...", show_alert=False)

    try:
        text = await render_top()

        kb = InlineKeyboardBuilder()
        kb.button(
            text=" ",
            icon_custom_emoji_id="5346269127059196142",
            callback_data="refresh_eyes"
        )
        kb.row(types.InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back"))

        await callback.message.edit_text(text, reply_markup=kb.as_markup())
    
    except Exception as e:
        logger.error(f"Error in refresh_eyes: {e}")


@router.message(F.text == "eyes")
async def stats_button(message: types.Message):
    await cmd_top(message)