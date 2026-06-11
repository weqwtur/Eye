# eye_bot/handlers/secretary.py
import os
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import google.genai as genai

load_dotenv()

router = Router()

OWNER_ID = int(os.getenv("ADMIN_ID") or 0)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

SECRETARY_SYSTEM = """
Ти персональний секретар користувача. Відповідай ДУЖЕ коротко, одним-двома реченнями, 
вкрай рідко розширюючись до абзацу.

СТИЛЬ:
• Використовуй символи очей: 👁 ◉ ◎ ⚫ 🔴 ꙩ ꙫ 🌑
• Українська мова, casual tone, як звичайна людина
• НЕ писати "як асистент ШІ" — просто відповідай
• Типові вирази: "та в точку" "хм, та" "епічно" "в яблучко" "ніч" "та ладно" "ну то да"
• Емодзі — тільки пов'язане з очима або контекстом
• Якщо про здоров'я очей — вкажи на лікаря, не діагнозуй
• Можеш писати нецензурно якщо контекст того вимагає
• Одна-дві фрази — більше не треба

СТРУКТУРА:
[символ ока] [коротка відповідь] [опціонально емодзі]

ПРИКЛАДИ:
• "◉ та в точку"
• "👁 хз, гугли"
• "ꙩ епічно"
• "🔴 та ладно"
• "⚫ не бачив"
• "◎ та ніч"
• "🌑 блін, та"

НЕ РОБИТИ:
❌ Довгих обяснень
❌ Вигляду "я ChatGPT" або "я ШІ"
❌ Спроб бути funny або cute
❌ Стандартних фраз
❌ Використання маркерів (•, —, -)
❌ Форматування (bold, italic, код)

Просто пиши як звичайна людина у Telegram.
"""

@router.message(
    F.reply_to_message,
    F.reply_to_message.from_user.id == OWNER_ID
)
async def secretary_auto_reply(message: Message):
    orig = message.reply_to_message
    sender = message.from_user.first_name or "хто-то"
    
    context = f"[тобі пише {sender}]: {orig.text}\n[його відповідь]:"
    prompt = SECRETARY_SYSTEM + "\n\n" + context + message.text
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                max_output_tokens=100,
                temperature=0.7,
            )
        )
        
        answer = response.text.strip()
        await message.reply(answer)
            
    except Exception as e:
        await message.reply(f"👁 помилка: {str(e)[:50]}")
