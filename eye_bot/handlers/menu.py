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
            InlineKeyboardButton(text="Other",    callback_data="menu:other"),
        ],
    ])


def other_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="GitHub", callback_data="menu:github"),
            InlineKeyboardButton(text="Report", callback_data="menu:report"),
        ],
        [
            InlineKeyboardButton(text="⭠ Back", callback_data="menu:back"),
            InlineKeyboardButton(text="Language", callback_data="menu:language"),
        ],
    ])



@router.message(Command("menu"), F.chat.type == "private")
async def cmd_menu(message: Message, state: FSMContext):
    await state.update_data(prev_menu="main")
    await message.answer("<b>Menu</b>", reply_markup=main_menu_kb(), parse_mode="HTML")



@router.callback_query(F.data == "menu:back", F.message.chat.type == "private")
async def cb_back(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    prev = data.get("prev_menu", "main")
    await state.clear()

    current_text = call.message.html_text

    if prev == "other":
        new_text = "<b>Other</b>"
        if current_text != new_text:
            await call.message.edit_text(new_text, reply_markup=other_menu_kb(), parse_mode="HTML")
    elif prev == "media":
        from eye_bot.handlers.media.router import media_menu_keyboard

        new_text = "📁 Choose media:"
        if current_text != new_text:
            await call.message.edit_text(new_text, reply_markup=media_menu_keyboard(), parse_mode="HTML")
    else:
        new_text = "<b>Menu</b>"
        if current_text != new_text:
            await call.message.edit_text(new_text, reply_markup=main_menu_kb(), parse_mode="HTML")

    await call.answer()




@router.callback_query(F.data == "menu:other", F.message.chat.type == "private")
async def cb_other(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="main")
    await call.message.edit_text("<b>Other</b>", reply_markup=other_menu_kb(), parse_mode="HTML")
    await call.answer()



@router.callback_query(F.data == "menu:diseases", F.message.chat.type == "private")
async def cb_diseases(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="main")
    from eye_bot.handlers.diseases.router import show_diseases_in_menu
    await call.answer()
    await show_diseases_in_menu(call.message)


@router.callback_query(F.data == "menu:media", F.message.chat.type == "private")
async def cb_media(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="main")
    from eye_bot.handlers.media.router import cmd_media
    await call.answer()
    await cmd_media(call.message)


@router.callback_query(F.data == "menu:facts", F.message.chat.type == "private")
async def cb_facts(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="main")
    from eye_bot.handlers.facts import cmd_facts
    await call.answer()
    await cmd_facts(call.message)


@router.callback_query(F.data == "menu:top", F.message.chat.type == "private")
async def cb_top(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="main")
    from eye_bot.handlers.top.router import show_top_in_menu
    await call.answer()
    await show_top_in_menu(call.message)


@router.callback_query(F.data == "menu:github", F.message.chat.type == "private")
async def cb_github(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="other")
    from eye_bot.handlers.github import show_github_in_menu
    await call.answer()
    await show_github_in_menu(call.message)


@router.callback_query(F.data == "menu:report", F.message.chat.type == "private")
async def cb_report(call: CallbackQuery, state: FSMContext):
    await state.update_data(prev_menu="other")
    from eye_bot.handlers.report import start_report_from_menu
    await call.answer()
    await start_report_from_menu(call.message, state)


@router.callback_query(F.data == "menu:sense", F.message.chat.type == "private")
async def cb_sense(call: CallbackQuery):
    await call.answer("👁️ Sense — coming soon!", show_alert=True)


@router.callback_query(F.data == "menu:language", F.message.chat.type == "private")
async def cb_language(call: CallbackQuery):
    await call.answer("🌐 Language — coming soon!", show_alert=True)
