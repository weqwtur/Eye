# eye_bot/handlers/secretary.py
import os
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message
import google.genai as genai
import logging

load_dotenv()

router = Router()

OWNER_ID = int(os.getenv("ADMIN_ID") or 0)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
logger = logging.getLogger(__name__)

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

@router.message(F.business_connection_id)
async def business_message_handler(message: Message):
    logger.info(f"🔍 ПЕРЕХОПЛЕНО: business_connection_id={message.business_connection_id}, text={message.text}")
    
    if not message.text:
        logger.warning("❌ Нема тексту")
        return
    
    sender = message.from_user.first_name or "хто-то"
    context = f"[тобі пише {sender}]: {message.text}"
    prompt = SECRETARY_SYSTEM + "\n\n" + context
    
    try:
        logger.info(f"🤖 Генеруємо через Gemini...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                max_output_tokens=100,
                temperature=0.7,
            )
        )
        
        answer = response.text.strip()
        logger.info(f"✅ Відповідь: {answer}")
        
        await message.reply(
            answer,
            business_connection_id=message.business_connection_id
        )
        logger.info(f"✉️ Відправлено успішно")
            
    except Exception as e:
        logger.error(f"❌ Помилка: {e}", exc_info=True)


@router.message()
async def catch_all(message: Message):
    logger.info(f"📩 Усе інше: {message.message_id}, business_connection_id={message.business_connection_id}, text={message.text[:50] if message.text else 'None'}")
