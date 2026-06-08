from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()



def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Diseases", callback_data="menu:diseases"),
            InlineKeyboardButton(text="Media",    callback_data="menu:media"),
        ],
        [
            InlineKeyboardButton(text="Facts",    callback_data="menu:facts"),
            InlineKeyboardButton(text="Top",      callback_data="menu:top"),
        ],
        [
            InlineKeyboardButton(text="Sense",    callback_data="menu:sense"),
            InlineKeyboardButton(text="Other",     callback_data="menu:other"),
        ],
    ])


def other_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="GitHub",   callback_data="menu:github"),
            InlineKeyboardButton(text="Report",   callback_data="menu:report"),
        ],
        [
            InlineKeyboardButton(text="⬅",     callback_data="menu:back"),
            InlineKeyboardButton(text="Language", callback_data="menu:language"),
        ],
    ])


def back_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Menu", callback_data="menu:back")]
    ])



@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(
        "<b>Menu</b>",
        reply_markup=main_menu_kb(),
        parse_mode="HTML",
    )



@router.callback_query(F.data == "menu:back")
async def cb_back(call: CallbackQuery):
    await call.message.edit_text(
        "<b>Menu</b>",
        reply_markup=main_menu_kb(),
        parse_mode="HTML",
    )
    await call.answer()


@router.callback_query(F.data == "menu:other")
async def cb_other(call: CallbackQuery):
    await call.message.edit_text(
        "<b>Other</b>",
        reply_markup=other_menu_kb(),
        parse_mode="HTML",
    )
    await call.answer()



@router.callback_query(F.data == "menu:diseases")
async def cb_diseases(call: CallbackQuery):
    await call.answer("🔬 Diseases — coming soon!", show_alert=True)


@router.callback_query(F.data == "menu:sense")
async def cb_sense(call: CallbackQuery):
    await call.answer("👁️ Sense — coming soon!", show_alert=True)


@router.callback_query(F.data == "menu:language")
async def cb_language(call: CallbackQuery):
    await call.answer("🌐 Language — coming soon!", show_alert=True)


@router.callback_query(F.data == "menu:media")
async def cb_media(call: CallbackQuery):
    from commands.media.media import cmd_media
    await call.answer()
    await cmd_media(call.message)


@router.callback_query(F.data == "menu:facts")
async def cb_facts(call: CallbackQuery):
    from commands.facts import cmd_facts
    await call.answer()
    await cmd_facts(call.message)


@router.callback_query(F.data == "menu:top")
async def cb_top(call: CallbackQuery):
    from commands.top.top import show_top_in_menu
    await call.answer()
    await show_top_in_menu(call.message)


@router.callback_query(F.data == "menu:github")
async def cb_github(call: CallbackQuery):
    from commands.github import show_github_in_menu
    await call.answer()
    await show_github_in_menu(call.message)


@router.callback_query(F.data == "menu:report")
async def cb_report(call: CallbackQuery, state: FSMContext):
    from commands.report import start_report_from_menu
    await call.answer()
    await start_report_from_menu(call.message, state)
