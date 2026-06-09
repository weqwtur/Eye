import os
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)


class ReportState(StatesGroup):
    waiting_for_text = State()


def report_back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭠ Back", callback_data="menu:back")]
    ])


async def start_report_from_menu(message: types.Message, state: FSMContext):
    await state.update_data(menu_message_id=message.message_id, prev_menu="other")
    await message.edit_text("Write your report:", reply_markup=report_back_keyboard())
    await state.set_state(ReportState.waiting_for_text)


@router.message(ReportState.waiting_for_text, F.chat.type == "private")
async def receive_report(message: types.Message, state: FSMContext):
    data = await state.get_data()
    menu_message_id = data.get("menu_message_id")

    user = message.from_user
    text = message.text or message.caption or ""
    photo = message.photo[-1].file_id if message.photo else None
    doc = message.document.file_id if message.document else None

    admin_header = (
        f"Message:\n"
        f"{text or '[media]'}\n\n"
        f"<code>/reply {user.id}</code>"
    )

    await message.bot.send_message(ADMIN_ID, admin_header)

    if photo:
        await message.bot.send_photo(ADMIN_ID, photo)
    if doc:
        await message.bot.send_document(ADMIN_ID, doc)

    await state.clear()
    await message.answer("Your report has been sent.")

    if menu_message_id:
        from eye_bot.handlers.menu import other_menu_kb

        await message.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=menu_message_id,
            text="<b>Other</b>",
            parse_mode="HTML",
            reply_markup=other_menu_kb()
        )


@router.message(Command("reply"))
async def admin_reply(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("Usage: /reply <user_id> <text>")
        return

    target_id = parts[1]
    text = parts[2]

    try:
        await message.bot.send_message(target_id, text)
        await message.answer("Delivered.")
    except Exception:
        await message.answer("Failed to deliver (maybe blocked).")
