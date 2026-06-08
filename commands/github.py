import logging
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()
logger = logging.getLogger(__name__)

GITHUB_URL = "https://t.me/WhatAnEyeBot/github"

GITHUB_MESSAGE = (
   "<blockquote>"
   "<pre><code class=\"language-python\">"
   "import webbrowser\n"
   "\n"
   "repo = {\n"
   "    'name': 'WhatAnEyeBot',\n"
   "    'source': 'telegram mini app',\n"
   "    'status': 'open',\n"
   "}\n"
   "\n"
   "webbrowser.open(repo['source'])"
   "</code></pre>"
   "</blockquote>"
)


@router.message(Command("github"))
async def cmd_github(message: types.Message):
   builder = InlineKeyboardBuilder()
   builder.button(
       text="Open Repository",
       url=GITHUB_URL
   )

   await message.answer(
       GITHUB_MESSAGE,
       parse_mode="HTML",
       reply_markup=builder.as_markup()
   )


async def show_github_in_menu(message: types.Message):
   """Called from menu - edits the existing message"""
   builder = InlineKeyboardBuilder()
   builder.button(
       text="Open Repository",
       url=GITHUB_URL
   )
   builder.row(InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back"))

   await message.edit_text(
       GITHUB_MESSAGE,
       parse_mode="HTML",
       reply_markup=builder.as_markup()
   )
