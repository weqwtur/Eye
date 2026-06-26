import asyncio
import logging
from typing import Optional

from aiogram import types
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .media_data import MEDIA_MAP, MediaItem

logger = logging.getLogger(__name__)
MEDIA_LOCKS: dict[int, asyncio.Lock] = {}

def _build_keyboard(media_id: int, index: int, total: int, tiktok: str | None):
    kb = InlineKeyboardBuilder()

    if tiktok:
        kb.row(types.InlineKeyboardButton(text=" ", url=tiktok))

    nav_buttons = []
    if index > 0:
        nav_buttons.append(
            types.InlineKeyboardButton(text="⭠", callback_data=f"media{media_id}:{index-1}")
        )
    
    back_to_menu = types.InlineKeyboardButton(text="⭠ Back", callback_data="open_media_menu")
    
    if index < total - 1:
        next_btn = types.InlineKeyboardButton(text="⭢", callback_data=f"media{media_id}:{index+1}")
        if index == 0:
            kb.row(back_to_menu, next_btn)
        else:
            kb.row(*nav_buttons, next_btn)
            kb.row(back_to_menu)
    else:
        kb.row(*nav_buttons)
        kb.row(back_to_menu)

    return kb.as_markup()

async def media_start(media_id: int, message_or_callback, index: int = 0):
    group: Optional[MediaItem] = MEDIA_MAP.get(media_id)
    if not group:
        await message_or_callback.answer("This media is not added yet")
        return

    items = group["items"]
    tiktok = group["tiktok"]
    file_type = group["type"]

    if index < 0 or index >= len(items):
        await message_or_callback.answer("❌ Invalid media index")
        return

    file_id = items[index]
    total = len(items)
    caption = f"· {index + 1} / {total} ·"
    markup = _build_keyboard(media_id, index, total, tiktok)

    try:
        if isinstance(message_or_callback, types.CallbackQuery):
            media = (
                types.InputMediaPhoto(media=file_id, caption=caption)
                if file_type == "photo"
                else types.InputMediaVideo(media=file_id, caption=caption)
            )
            await message_or_callback.message.edit_media(media=media, reply_markup=markup)
            await message_or_callback.answer()
        else:
            if file_type == "photo":
                await message_or_callback.answer_photo(
                    photo=file_id,
                    caption=caption,
                    reply_markup=markup
                )
            else:
                await message_or_callback.answer_video(
                    video=file_id,
                    caption=caption,
                    reply_markup=markup
                )

    except TelegramBadRequest as e:
        logger.error(f"BadRequest sending media {media_id}[{index}]: {e}", exc_info=True)
        try:
            await message_or_callback.answer("❌ This media file is unavailable or has been removed.")
        except Exception as answer_error:
            logger.error(f"Error answering BadRequest: {answer_error}", exc_info=True)
    except Exception as e:
        logger.error(f"Error sending media {media_id}[{index}]: {e}", exc_info=True)
        try:
            await message_or_callback.answer("❌ Error sending media")
        except Exception as answer_error:
            logger.error(f"Error answering generic exception: {answer_error}", exc_info=True)
