import logging
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

router = Router()
logger = logging.getLogger(__name__)

DISEASES_URL = "https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases"

DISEASES_MESSAGE = "Diseases and Conditions"


async def show_diseases_in_menu(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Website", url=DISEASES_URL)
    builder.row(InlineKeyboardButton(text="⭠ Back", callback_data="menu:back"))

    await message.edit_text(
        DISEASES_MESSAGE,
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )
