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
Ти персональний секретар користувача. Відповідай ДУЖЕ коротко одним-двома реченнями.
Українська, casual tone. Символи очей: 👁 ◉ ◎ ⚫ 🔴 ꙩ ꙫ 🌑
Типові вирази: "та в точку" "хм, та" "епічно" "та ладно"
Просто пиши як звичайна людина у Telegram.
"""

@router.message(F.business_connection_id)
async def business_message_handler(message: Message):
    logger.info(f"🔍 business_connection_id: {message.business_connection_id}")
    logger.info(f"📩 Текст: {message.text}")
    
    if not message.text:
        logger.warning("❌ Нема тексту")
        return
    
    sender = message.from_user.first_name or "хто-то"
    context = f"[тобі пише {sender}]: {message.text}"
    prompt = SECRETARY_SYSTEM + "\n\n" + context
    
    try:
        logger.info(f"🤖 Генеруємо відповідь...")
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
        logger.info(f"✉️ Відправлено")
            
    except Exception as e:
        logger.error(f"❌ Помилка Gemini: {e}", exc_info=True)
        try:
            await message.reply(f"👁 помилка: {str(e)[:50]}", business_connection_id=message.business_connection_id)
        except Exception as e2:
            logger.error(f"❌ Помилка при відправці: {e2}")
