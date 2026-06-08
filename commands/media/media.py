import logging
from aiogram import Router, types, F, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os

router = Router()
logger = logging.getLogger(__name__)

ADMIN_ID = int(os.getenv("ADMIN_ID"))


class MediaSuggest(StatesGroup):
    waiting_for_link = State()


def media_menu_keyboard():
    kb = InlineKeyboardBuilder()
    for i in range(1, 10):
        kb.button(text=f"{i}", callback_data=f"open_media:{i}")
    kb.adjust(3, 3, 3)
    kb.row(types.InlineKeyboardButton(
        text="📤 Suggest media",
        callback_data="suggest_media"
    ))
    kb.row(types.InlineKeyboardButton(
        text="⬅ Back to Menu",
        callback_data="menu:back"
    ))
    return kb.as_markup()


async def cmd_media(message: types.Message):
    await message.edit_text("📁 Choose media:", reply_markup=media_menu_keyboard())


@router.callback_query(F.data == "suggest_media", F.message.chat.type == "private")
async def suggest_media_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(MediaSuggest.waiting_for_link)
    await state.update_data(menu_message_id=callback.message.message_id)
    await callback.message.edit_text("📤 Send a link to your media:")
    await callback.answer()


@router.callback_query(F.data == "menu:back", F.message.chat.type == "private")
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("📁 Choose media:", reply_markup=media_menu_keyboard())
    await callback.answer()


@router.message(MediaSuggest.waiting_for_link, F.text, F.chat.type == "private")
async def suggest_media_receive(message: types.Message, state: FSMContext, bot: Bot):
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

    await message.reply("✅ Thank you! Your link to the media file has been sent for review.")

    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=menu_message_id,
        text="📁 Choose media:",
        reply_markup=media_menu_keyboard()
    )


@router.callback_query(F.data.startswith("open_media:"), F.message.chat.type == "private")
async def open_media(callback: types.CallbackQuery):
    media_id = int(callback.data.split(":")[1])

    if media_id == 1:
        from commands.media.media1 import media1_start
        return await media1_start(callback.message)
    if media_id == 2:
        from commands.media.media2 import media2_start
        return await media2_start(callback.message)
    if media_id == 3:
        from commands.media.media3 import media3_start
        return await media3_start(callback.message)
    if media_id == 4:
        from commands.media.media4 import media4_start
        return await media4_start(callback.message)
    if media_id == 5:
        from commands.media.media5 import media5_start
        return await media5_start(callback.message)
    if media_id == 6:
        from commands.media.media6 import media6_start
        return await media6_start(callback.message)
    if media_id == 7:
        from commands.media.media7 import media7_start
        return await media7_start(callback.message)
    if media_id == 8:
        from commands.media.media8 import media8_start
        return await media8_start(callback.message)
    if media_id == 9:
        from commands.media.media9 import media9_start
        return await media9_start(callback.message)

    await callback.answer("This media is not added yet")
