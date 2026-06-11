# eye_bot/handlers/secretary.py
import os
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message
import google.genai as genai

load_dotenv()

router = Router()

OWNER_ID = int(os.getenv("ADMIN_ID") or 0)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

SECRETARY_SYSTEM = """
Ти персональний секретар користувача. Відповідай ДУЖЕ коротко.

СТИЛЬ:
• Символи очей: 👁 ◉ ◎ ⚫ 🔴 ꙩ ꙫ 🌑
• Українська, casual tone
• Типові вирази: "та в точку" "хм, та" "епічно" "та ладно" "ну то да"
• Одна-дві фрази — більше не треба
• Емодзі — тільки зі очима

Просто пиши як звичайна людина у Telegram без ШІ вигляду.
"""

@router.message()
async def secretary_handler(message: Message):
    if message.from_user.id == OWNER_ID:
        return
    
    if not message.text:
        return
    
    sender = message.from_user.first_name or "хто-то"
    context = f"[тобі пише {sender}]: {message.text}"
    prompt = SECRETARY_SYSTEM + "\n\n" + context
    
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
        pass
