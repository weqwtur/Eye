# eye_bot/handlers/secretary.py
import os
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import google.generativeai as genai

load_dotenv()

router = Router()

OWNER_ID = int(os.getenv("ADMIN_ID") or 0)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

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

@router.message(F.from_user.id == OWNER_ID)
async def secretary_process(message: Message):
    context = ""
    if message.reply_to_message:
        orig = message.reply_to_message
        sender = orig.from_user.first_name if orig.from_user else "хто-то"
        context = f"[контекст] {sender}: {orig.text}\n"
    
    try:
        prompt = SECRETARY_SYSTEM + "\n\n" + context + message.text
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=100,
                temperature=0.7,
            )
        )
        
        answer = response.text.strip()
        
        if message.reply_to_message:
            await message.reply_to_message.reply(answer)
        else:
            await message.reply(answer)
            
    except Exception as e:
        await message.reply(f"👁 помилка: {str(e)[:50]}")


@router.message(Command("ок"), F.from_user.id == OWNER_ID)
async def manual_respond(message: Message):
    if not message.reply_to_message:
        await message.answer("👁 reply на повідомлення")
        return
    
    text = message.text.replace("/ок", "").strip()
    if not text:
        await message.answer("👁 текст?")
        return
    
    try:
        prompt = SECRETARY_SYSTEM + "\n\n" + text
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=100,
                temperature=0.7,
            )
        )
        
        answer = response.text.strip()
        await message.reply_to_message.reply(answer)
        
    except Exception as e:
        await message.reply(f"👁 помилка: {str(e)[:50]}")
