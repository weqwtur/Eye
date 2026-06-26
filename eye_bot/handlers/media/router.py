import logging
import os
import re
import time
import asyncio

from aiogram import Router, Bot, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from . import gallery
from .media_data import MEDIA_MAP

router = Router()
logger = logging.getLogger(__name__)

ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)

SUGGESTION_WINDOW_SECONDS = 5 * 60
SUGGESTION_LIMIT = 3

suggestion_timestamps: dict[int, list[float]] = {}
blacklisted_suggest_users: set[int] = set()

VALID_URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)


class MediaSuggest(StatesGroup):
    waiting_for_link = State()
    waiting_for_confirm = State()


def media_menu_keyboard():
    kb = InlineKeyboardBuilder()

    for i in range(1, len(MEDIA_MAP) + 1):
        kb.button(text=str(i), callback_data=f"open_media:{i}")

    kb.adjust(3, 3, 3)

    kb.row(types.InlineKeyboardButton(text="Suggest media", callback_data="suggest_media"))
    kb.row(types.InlineKeyboardButton(text="⭠ Back", callback_data="menu:back"))

    return kb.as_markup()


def suggest_back_keyboard():
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="⭠ Back", callback_data="menu:back"))
    return kb.as_markup()


def confirm_suggest_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Confirm", callback_data="confirm_suggest")
    kb.button(text="❌ Cancel", callback_data="cancel_suggest")
    kb.adjust(2)
    return kb.as_markup()


def _cleanup_suggestion_timestamps(user_id: int) -> list[float]:
    now = time.time()
    timestamps = [
        ts for ts in suggestion_timestamps.get(user_id, [])
        if now - ts < SUGGESTION_WINDOW_SECONDS
    ]

    if timestamps:
        suggestion_timestamps[user_id] = timestamps
    else:
        suggestion_timestamps.pop(user_id, None)

    return timestamps


def _has_suggestion_quota(user_id: int) -> bool:
    return len(_cleanup_suggestion_timestamps(user_id)) < SUGGESTION_LIMIT


async def cmd_media(message: types.Message):
    await message.edit_text("📁 Choose media:", reply_markup=media_menu_keyboard())


@router.callback_query(F.data == "suggest_media", F.message.chat.type == "private")
async def suggest_media_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(MediaSuggest.waiting_for_link)
    await state.update_data(menu_message_id=callback.message.message_id)

    await callback.message.edit_text(
        "📤 Send a link to your media:",
        reply_markup=suggest_back_keyboard()
    )
    await callback.answer()


@router.message(MediaSuggest.waiting_for_link, F.photo | F.video, F.chat.type == "private")
async def suggest_media_waiting_for_image(message: types.Message):
    await message.reply("Please send a text link to your media instead of a photo or video.")


@router.message(MediaSuggest.waiting_for_link, F.text, F.chat.type == "private")
async def suggest_media_receive(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if user_id in blacklisted_suggest_users:
        await message.reply("You are not allowed to submit media suggestions at this time.")
        return

    match = VALID_URL_PATTERN.search(message.text or "")
    if not match:
        await message.reply("Please send a valid link starting with http:// or https://.")
        return

    if not _has_suggestion_quota(user_id):
        await message.reply("You can submit up to 3 suggestions every 5 minutes. Try again later.")
        return

    url = match.group(0)
    await state.update_data(pending_link=url)
    await state.set_state(MediaSuggest.waiting_for_confirm)

    await message.reply(
        f"Please confirm your media suggestion:\n\n{url}",
        reply_markup=confirm_suggest_keyboard()
    )


@router.callback_query(F.data == "confirm_suggest", F.message.chat.type == "private")
async def suggest_media_confirm(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    url = data.get("pending_link")
    menu_message_id = data.get("menu_message_id")
    user_id = callback.from_user.id

    if not url:
        await callback.answer("No media link to confirm.")
        return

    if not _has_suggestion_quota(user_id):
        await callback.answer("You can submit up to 3 suggestions every 5 minutes.")
        return

    suggestion_timestamps.setdefault(user_id, []).append(time.time())

    await bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            f"📬 New media suggestion from "
            f"<b>{callback.from_user.full_name}</b> "
            f"(<code>{user_id}</code>)\n\n{url}"
        ),
        parse_mode="HTML"
    )

    await state.clear()

    await callback.message.edit_text("✅ Thank you! Your link has been sent for review.")

    if menu_message_id:
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=menu_message_id,
            text="📁 Choose media:",
            reply_markup=media_menu_keyboard()
        )

    await callback.answer()


@router.callback_query(F.data == "cancel_suggest", F.message.chat.type == "private")
async def suggest_media_cancel(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    menu_message_id = data.get("menu_message_id")

    await state.clear()

    if menu_message_id:
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=menu_message_id,
            text="📁 Choose media:",
            reply_markup=media_menu_keyboard()
        )

    await callback.answer("Suggestion canceled.")


@router.message(F.from_user.id == ADMIN_ID, F.text.regexp(r"^/ban_suggest\s+\d+$"))
async def ban_suggest_command(message: types.Message):
    user_id = int(message.text.split()[1])
    blacklisted_suggest_users.add(user_id)
    await message.reply(f"User {user_id} has been banned from media suggestions.")


@router.message(F.from_user.id == ADMIN_ID, F.text.regexp(r"^/unban_suggest\s+\d+$"))
async def unban_suggest_command(message: types.Message):
    user_id = int(message.text.split()[1])
    blacklisted_suggest_users.discard(user_id)
    await message.reply(f"User {user_id} has been unbanned from media suggestions.")


@router.callback_query(F.data.startswith("open_media:"), F.message.chat.type == "private")
async def open_media(callback: types.CallbackQuery):
    media_id = int(callback.data.split(":")[1])

    try:
        await gallery.media_start(media_id, callback, index=0)
    except Exception as e:
        logger.error(f"Error opening media {media_id}: {e}", exc_info=True)
        await callback.answer("This media is not added yet")


@router.callback_query(F.data.regexp(r"^media\d+:\d+$"), F.message.chat.type == "private")
async def media_switch(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lock = gallery.MEDIA_LOCKS.setdefault(user_id, asyncio.Lock())

    try:
        if hasattr(lock, "acquire_nowait"):
            lock.acquire_nowait()
        else:
            if lock.locked():
                await callback.answer()
                return
            await lock.acquire()
    except RuntimeError:
        await callback.answer()
        return

    try:
        media_id, index = map(int, callback.data.replace("media", "").split(":"))
        await gallery.media_start(media_id, callback, index=index)
    except Exception as e:
        logger.error(f"Error switching media for {callback.data}: {e}", exc_info=True)
        await callback.answer("❌ Error")
    finally:
        if lock.locked():
            lock.release()


@router.callback_query(F.data == "open_media_menu", F.message.chat.type == "private")
async def back_to_media_menu(callback: types.CallbackQuery):
<<<<<<< HEAD
    await callback.message.edit_text("📁 Choose media:", reply_markup=media_menu_keyboard())
=======
    msg = callback.message

    # Media messages (photo/video) can't be edited as text — delete and resend
    if msg.photo or msg.video or msg.animation:
        try:
            await msg.delete()
            await msg.answer("📁 Choose media:", reply_markup=media_menu_keyboard())
        except Exception as e:
            logger.error(f"Error returning to media menu: {e}", exc_info=True)
            try:
                await msg.edit_caption(caption="📁 Choose media:", reply_markup=media_menu_keyboard())
            except Exception:
                pass
    else:
        await msg.edit_text("📁 Choose media:", reply_markup=media_menu_keyboard())

>>>>>>> 846992e (upd)
    await callback.answer()