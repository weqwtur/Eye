import os
import logging
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message
import google.genai as genai
from google.genai.errors import ServerError, ClientError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

load_dotenv()

router = Router()

OWNER_ID = int(os.getenv("ADMIN_ID") or 0)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
logger = logging.getLogger(__name__)

SECRETARY_SYSTEM = "Ти персональний секретар користувача. Відповідай ДУЖЕ коротко."

@retry(
    retry=retry_if_exception_type((ServerError, ClientError)),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
async def generate_response(prompt: str, model_name: str = "models/gemini-3.5-flash"):
    """Функція для запиту до API з підтримкою повторних спроб."""
    return client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            max_output_tokens=100,
            temperature=0.7,
        )
    )

async def process_secretary_message(message: Message, business: bool = False):
    if not message.text:
        return

    sender = message.from_user.first_name or "хто-то"
    context = f"[тобі пише {sender}]: {message.text}"
    prompt = SECRETARY_SYSTEM + "\n\n" + context

    try:
        logger.info(f"💬 Обробляю: {message.text[:50]}")
        
        # Спроба з основною моделлю
        response = await generate_response(prompt, "models/gemini-3.5-flash")
        answer = response.text.strip()

    except Exception as e:
        logger.warning(f"⚠️ Основна модель не відповіла, спроба fallback: {e}")
        try:
            # Спроба з більш стабільною lite моделлю
            response = await generate_response(prompt, "models/gemini-3.1-flash-lite")
            answer = response.text.strip()
        except Exception as e2:
            logger.error(f"❌ Критична помилка після fallback: {e2}")
            await message.reply("Сервер AI зараз перевантажений. Спробуй через хвилину.")
            return

    reply_kwargs = {}
    if business and getattr(message, "business_connection_id", None):
        reply_kwargs["business_connection_id"] = message.business_connection_id

    await message.reply(answer, **reply_kwargs)
    logger.info(f"✅ Відповідь: {answer}")


@router.message(F.chat.type == "private", F.text)
async def private_secretary(message: Message):
    await process_secretary_message(message)


@router.business_message(F.text)
async def business_secretary(message: Message):
    await process_secretary_message(message, business=True)