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

# Додайте свій ID у .env, щоб бот знав, на чиї повідомлення не відповідати
MY_ID = int(os.getenv("MY_ID", 0)) 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
logger = logging.getLogger(__name__)

# Використовуємо стабільну модель без "Thinking" (2.0-flash)
STABLE_MODEL = "models/gemini-2.5-flash-light"

SECRETARY_SYSTEM = "Ти персональний секретар. Відповідай дуже коротко. Ігноруй внутрішні міркування, видавай лише фінальний текст відповіді."

@retry(
    retry=retry_if_exception_type((ServerError, ClientError)),
    stop=stop_after_attempt(2),
    wait=wait_exponential(multiplier=1, min=1, max=5)
)
async def generate_response(prompt: str, model_name: str):
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=genai.types.GenerateContentConfig(max_output_tokens=100, temperature=0.7)
    )
    
    # ПРАВИЛЬНИЙ ЗБІР ТЕКСТУ (ігноруємо thought_signature)
    full_text = "".join([part.text for part in response.candidates[0].content.parts if part.text])
    return full_text.strip()

async def process_secretary_message(message: Message, business: bool = False):
    # ФІЛЬТРАЦІЯ: не відповідаємо на свої ж повідомлення
    if message.from_user.id == MY_ID:
        return

    if not message.text:
        return

    prompt = f"{SECRETARY_SYSTEM}\n\n[Користувач {message.from_user.first_name}]: {message.text}"

    try:
        logger.info(f"💬 Обробляю: {message.text[:30]}")
        answer = await generate_response(prompt, STABLE_MODEL)
    except Exception as e:
        logger.warning(f"⚠️ Модель не відповіла: {e}")
        return # Краще мовчати, ніж спамити помилками в бізнес-чаті

    reply_kwargs = {}
    if business and getattr(message, "business_connection_id", None):
        reply_kwargs["business_connection_id"] = message.business_connection_id

    await message.reply(answer, **reply_kwargs)
    logger.info(f"✅ Відповідь: {answer}")


@router.business_message(F.text)
async def business_secretary(message: Message):
    # Додаємо умову: відповідаємо тільки якщо це не бот і не ми
    if not message.from_user.is_bot:
        await process_secretary_message(message, business=True)