from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging

logger = logging.getLogger(__name__)

# Consolidated media lists from original media1..media9
TT_LINK = "https://vt.tiktok.com/"

MEDIA_MAP = {
    1: [
        "AgACAgIAAxkBAAN0ahPG9xUhMooCg3qfFr-rD-R8QvUAAiAYaxvFuaBIaFY9nINsWLkBAAMCAAN4AAM7BA",
        "AgACAgIAAxkBAAN2ahPHF54KRGTej5A2JVSzc8bfSYsAAiEYaxvFuaBIOKHXTv_xA4sBAAMCAAN4AAM7BA",
        "AgACAgIAAxkBAAN4ahPHHeBZRbMDPp9aAAFgy9exuSeLAAIiGGsbxbmgSFtQHBmxYmq_AQADAgADeAADOwQ",
    ],
    2: ["BAACAgIAAxkBAAOYahPNKl8PTF6LQNYaxvM5I-bgohAAAmGSAALFuaBILU7OlNVrCeM7BA"],
    3: ["BAACAgIAAxkBAAOeahPPURZv3xHdIdK8niUdOTAGS_oAAmuSAALFuaBIXIhc4qhJVPg7BA"],
    4: ["BAACAgIAAxkBAAOgahPQFkXt0HCUKZG14JbMp_P-yaIAAnGSAALFuaBIClqMvFu6jUU7BA"],
    5: ["BAACAgIAAxkBAAICY2oVEY0oyy-FKUoukUW6Vegnjt22AAKYkgACxbmoSNUPUdmkzbWqOwQ"],
    6: ["BAACAgIAAxkBAAOpahPRq7BOXO6z8bkbK_Wyun9FP1UAAnmSAALFuaBIGeAHoMcBIg87BA"],
    7: ["BAACAgIAAxkBAAPIahPm_lCYp8Lxr6Mo_RTur8dehaAAAviSAALFuaBIvJD0UJCJn6o7BA"],
    8: ["BAACAgIAAxkBAAPKahPnaKrPTXf2UXC11V_Wjpf1VyAAAvySAALFuaBIsD2XkZulew87BA"],
    9: [
        "AgACAgIAAxkBAAPMahPp0nq3Puq8xUmkAUIEkvYMDakAAqcaaxvFuaBI9v9-Ai1ca30BAAMCAAN5AAM7BA",
        "AgACAgIAAxkBAAPNahPp0ksAAQhAoGJ2jMT8W34Q4CcuAAKoGmsbxbmgSIvdVgJGJNGzAQADAgADeQADOwQ",
    ],
}


async def media_start(media_id: int, message_or_callback, index: int = 0):
    media_list = MEDIA_MAP.get(media_id)
    if not media_list:
        await message_or_callback.answer("This media is not added yet")
        return

    if index < 0 or index >= len(media_list):
        await message_or_callback.answer("❌ Invalid media index")
        return

    kb = InlineKeyboardBuilder()
    kb.button(text=" ", url=TT_LINK)

    if index > 0:
        kb.button(text="⭠", callback_data=f"media{media_id}:{index-1}")

    if index < len(media_list) - 1:
        kb.button(text="⭢", callback_data=f"media{media_id}:{index+1}")

    kb.adjust(1, 2)

    file_id = media_list[index]

    try:
        if file_id.startswith("AgAC") or file_id.startswith("BQAC"):
            await message_or_callback.answer_photo(photo=file_id, reply_markup=kb.as_markup())
        else:
            await message_or_callback.answer_video(video=file_id, reply_markup=kb.as_markup())
    except Exception as e:
        logger.error(f"Error sending media {media_id}[{index}]: {e}")
        try:
            await message_or_callback.answer("❌ Error sending media")
        except Exception:
            pass
