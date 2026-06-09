import os
from aiogram import Router, types, F
from dotenv import load_dotenv

load_dotenv()

router = Router()

ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)


@router.message(
    F.from_user.id == ADMIN_ID,
    F.content_type.in_({"photo", "animation", "video", "document", "sticker"})
)
async def admin_file_id(message: types.Message):

    if message.photo:
        return await message.answer(
            f"📸 Photo file_id:\n<code>{message.photo[-1].file_id}</code>"
        )

    if message.animation:
        return await message.answer(
            f"🎞 GIF file_id:\n<code>{message.animation.file_id}</code>"
        )

    if message.video:
        return await message.answer(
            f"🎥 Video file_id:\n<code>{message.video.file_id}</code>"
        )

    if message.document:
        return await message.answer(
            f"📄 Document file_id:\n<code>{message.document.file_id}</code>"
        )

    if message.sticker:
        return await message.answer(
            f"🔖 Sticker file_id:\n<code>{message.sticker.file_id}</code>"
        )
