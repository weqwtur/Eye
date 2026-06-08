from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

TT_LINK = "https://vt.tiktok.com/ZSxuaGqyR/"

MEDIA = [
    "AgACAgIAAxkBAAN0ahPG9xUhMooCg3qfFr-rD-R8QvUAAiAYaxvFuaBIaFY9nINsWLkBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAN2ahPHF54KRGTej5A2JVSzc8bfSYsAAiEYaxvFuaBIOKHXTv_xA4sBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAN4ahPHHeBZRbMDPp9aAAFgy9exuSeLAAIiGGsbxbmgSFtQHBmxYmq_AQADAgADeAADOwQ",
    "AgACAgIAAxkBAAOAahPKTG72Sx1lKG3D-EIQVZILODsAAiwYaxvFuaBIHdcWd0YbHukBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOCahPKUNf5hwYdtTntjLHWsoainTAAAi0YaxvFuaBIoSBTenLS0JIBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOEahPKUyPhEPNNN3HiE_ZJ79cNKwUAAi4YaxvFuaBIk4ADuzrNR7sBAAMCAAN5AAM7BA",
    "AgACAgIAAxkBAAOGahPKVkji6OtI4igqk7vgV9ZIbBUAAi8YaxvFuaBIB_OULEKwXAsBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOIahPKWb17vTyePcah1f63cwEEtlcAAjAYaxvFuaBIDVnFyQeHraIBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOKahPKXPEguXal8BNKZpI8KvTfl28AAjEYaxvFuaBI9OWsJFUH3ygBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOMahPKXtFqOnalf502_Cy5c5HBkvYAAjIYaxvFuaBIyEjqDL6XzaoBAAMCAAN5AAM7BA",
    "AgACAgIAAxkBAAOOahPKYb-lv3RssUnD89FRnD-WiUsAAjMYaxvFuaBIAAFXw4brc2bCAQADAgADeAADOwQ",
    "AgACAgIAAxkBAAOQahPKY8XUV-Qeguvbnz58SkG8QLMAAjQYaxvFuaBI4ZhL8DdfYQIBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOSahPKZlgSZQmu3mMyga7P3jcVSrcAAjUYaxvFuaBIbsT3yXNJ7LcBAAMCAAN4AAM7BA",
    "AgACAgIAAxkBAAOUahPKaXSLTlqm76IorPEiRVC0pEgAAjYYaxvFuaBIrQd4ufLSWKABAAMCAAN4AAM7BA"
]


async def media1_start(message: types.Message):
    await send_media(message, index=0)


async def send_media(message_or_callback, index: int):
    kb = InlineKeyboardBuilder()

    kb.button(text=" ", url=TT_LINK)

    if index > 0:
        kb.button(text="⬅", callback_data=f"media1:{index-1}")

    if index < len(MEDIA) - 1:
        kb.button(text="⭢", callback_data=f"media1:{index+1}")

    kb.adjust(1, 2)

    file_id = MEDIA[index]

    if file_id.startswith("AgAC") or file_id.startswith("BQAC"):
        await message_or_callback.answer_photo(
            photo=file_id,
            reply_markup=kb.as_markup()
        )
    else:
        await message_or_callback.answer_video(
            video=file_id,
            reply_markup=kb.as_markup()
        )


@router.callback_query(F.data.startswith("media1:"))
async def media1_switch(callback: types.CallbackQuery):
    index = int(callback.data.split(":")[1])

    kb = InlineKeyboardBuilder()

    kb.button(text=" ", url=TT_LINK)

    if index > 0:
        kb.button(text="⬅", callback_data=f"media1:{index-1}")

    if index < len(MEDIA) - 1:
        kb.button(text="⭢", callback_data=f"media1:{index+1}")

    kb.adjust(1, 2)

    file_id = MEDIA[index]

    try:
        await callback.message.edit_media(
            media=types.InputMediaPhoto(media=file_id)
            if file_id.startswith("AgAC") or file_id.startswith("BQAC")
            else types.InputMediaVideo(media=file_id),
            reply_markup=kb.as_markup()
        )
    except:
        pass

    await callback.answer()
