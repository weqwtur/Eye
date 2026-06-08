import os

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

ADMIN_ID = int(os.getenv("ADMIN_ID"))

class ReportState(StatesGroup):
    waiting_for_text = State()


@router.message(Command("report"), F.chat.type == "private")
async def report_start(message: types.Message, state: FSMContext):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back")]
    ])
    await message.answer("Write your report:", reply_markup=kb)
    await state.set_state(ReportState.waiting_for_text)


async def start_report_from_menu(message: types.Message, state: FSMContext):
    """Called from menu - edits the existing message"""
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back")]
    ])
    await message.edit_text("Write your report:", reply_markup=kb)
    await state.set_state(ReportState.waiting_for_text)


@router.message(ReportState.waiting_for_text, F.chat.type == "private")
async def receive_report(message: types.Message, state: FSMContext):
    user = message.from_user

    text = message.text or message.caption or ""
    photo = message.photo[-1].file_id if message.photo else None
    doc = message.document.file_id if message.document else None

    admin_header = (
        f"Message:\n"
        f"{text or '[media]'}\n\n"
        f"<code>/reply {user.id}</code> "
    )

    await message.bot.send_message(ADMIN_ID, admin_header)

    if photo:
        await message.bot.send_photo(ADMIN_ID, photo)
    if doc:
        await message.bot.send_document(ADMIN_ID, doc)

    await message.answer("Your report has been sent.")
    await state.clear()


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
