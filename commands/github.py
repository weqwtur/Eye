import logging
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
async def github_command(message: types.Message):
   builder = InlineKeyboardBuilder()
   builder.button(
       text="Open Repository ",
       url=GITHUB_URL
   )

   await message.answer(
       GITHUB_MESSAGE,
       parse_mode="HTML",
       reply_markup=builder.as_markup()
   )
