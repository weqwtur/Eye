import logging
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os

router = Router()
logger = logging.getLogger(__name__)

ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)


class MediaSuggest(StatesGroup):
    waiting_for_link = State()



def media_menu_keyboard():
    kb = InlineKeyboardBuilder()

    # 9 media buttons
    for i in range(1, 10):
        kb.button(text=str(i), callback_data=f"open_media:{i}")
    kb.adjust(3, 3, 3)

    kb.row(
        types.InlineKeyboardButton(
            text="Suggest media",
            callback_data="suggest_media"
        )
    )

    # universal back (handled in menu.py)
    kb.row(
        types.InlineKeyboardButton(
            text="⭠ Back",
            callback_data="menu:back"
        )
    )

    return kb.as_markup()


def suggest_back_keyboard():
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(
            text="⭠ Back",
            callback_data="menu:back"
        )
    )
    return kb.as_markup()



async def cmd_media(message: types.Message):
    await message.edit_text(
        "📁 Choose media:",
        reply_markup=media_menu_keyboard()
    )



@router.callback_query(F.data == "suggest_media", F.message.chat.type == "private")
async def suggest_media_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(MediaSuggest.waiting_for_link)

    await state.update_data(menu_message_id=callback.message.message_id, prev_menu="media")

    await callback.message.edit_text(
        "📤 Send a link to your media:",
        reply_markup=suggest_back_keyboard()
    )
    await callback.answer()


@router.message(MediaSuggest.waiting_for_link, F.text, F.chat.type == "private")
async def suggest_media_receive(message: types.Message, state: FSMContext, bot: types.Bot):
    data = await state.get_data()
    menu_message_id = data.get("menu_message_id")

    await bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            f"📬 New media suggestion from "
            f"<b>{message.from_user.full_name}</b> "
            f"(<code>{message.from_user.id}</code>)\n\n"
            f"{message.text}"
        ),
        parse_mode="HTML"
    )

    await state.clear()

    await message.reply("✅ Thank you! Your link has been sent for review.")

    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=menu_message_id,
        text="📁 Choose media:",
        reply_markup=media_menu_keyboard()
    )



@router.callback_query(F.data.startswith("open_media:"), F.message.chat.type == "private")
async def open_media(callback: types.CallbackQuery):
    media_id = int(callback.data.split(":")[1])

    try:
        from eye_bot.handlers.media import gallery

        return await gallery.media_start(media_id, callback.message, index=0)
    except Exception:
        await callback.answer("This media is not added yet")


@router.callback_query(F.data.startswith("media"), F.message.chat.type == "private")
async def media_switch(callback: types.CallbackQuery):
    # pattern media{media_id}:{index}
    try:
        parts = callback.data.replace('media', '').split(":")
        media_id = int(parts[0])
        index = int(parts[1])

        from eye_bot.handlers.media import gallery

        await gallery.media_start(media_id, callback.message, index=index)
    except Exception:
        await callback.answer("❌ Error")
