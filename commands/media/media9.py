import logging
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
logger = logging.getLogger(__name__)

TT_LINK = "https://vt.tiktok.com/ZSxHkUaM9/"

MEDIA = [
    "AgACAgIAAxkBAAPMahPp0nq3Puq8xUmkAUIEkvYMDakAAqcaaxvFuaBI9v9-Ai1ca30BAAMCAAN5AAM7BA", #1
    "AgACAgIAAxkBAAPNahPp0ksAAQhAoGJ2jMT8W34Q4CcuAAKoGmsbxbmgSIvdVgJGJNGzAQADAgADeQADOwQ", #2
    "AgACAgIAAxkBAAPOahPp0kZ8FTHv_90f1VFYbzPQfNYAAqkaaxvFuaBIfxnYvN31h2IBAAMCAAN5AAM7BA", #3
    "AgACAgIAAxkBAAPYahPqCNruse_qBVVVajNHHsufz-YAAqsaaxvFuaBI-UJq6acqGWUBAAMCAAN5AAM7BA", #4
    "AgACAgIAAxkBAAPaahPqEuYV9v7YDNUL8ZDVKTKiMcYAAqwaaxvFuaBISednwn-gz2IBAAMCAAN5AAM7BA", #5
    "AgACAgIAAxkBAAPeahPqKQWGAAHajgHg9WCRWSsuIQtbAAK6GmsbxbmgSAtZxM4ongYMAQADAgADeQADOwQ", #6
    "AgACAgIAAxkBAAPiahPqQ_dnGYhfRUmwPDr66IHa3dEAAr4aaxvFuaBIlMJSQJxgeBsBAAMCAAN5AAM7BA", #7
    "AgACAgIAAxkBAAPkahPqTQAB3KKcZok0Rkf8zdtne9UKAAK_GmsbxbmgSLtkiK5sVeCNAQADAgADeQADOwQ", #8
    "AgACAgIAAxkBAAPmahPqV3_PIRgR09-MWfc3ghPP2s4AAsAaaxvFuaBIhLaknX0Voj8BAAMCAAN5AAM7BA", #9
    "AgACAgIAAxkBAAIBL2oT8xUZJ1XUKjalaxwh-f3Cd13mAAILHGsbxbmgSJ9vpaHEBbGaAQADAgADeQADOwQ", #10
    "AgACAgIAAxkBAAPqahPqaxnjUFGTX348eezPv1vAzQEAAsMaaxvFuaBIF3Vc-ZSup1IBAAMCAAN5AAM7BA", #11
    "AgACAgIAAxkBAAIBq2oUGExrEx03oFEbczTuW-Iwl5leAALfHmsbxbmgSJtQU7FOE5aQAQADAgADeQADOwQ", #12
    "AgACAgIAAxkBAAIBrWoUGGCAQKB3iH44RqDqYHFHlQnWAALgHmsbxbmgSM0dPQVX3ml9AQADAgADeQADOwQ", #13
    "AgACAgIAAxkBAAIBr2oUGITFodXr3YuF8ucgmr3suf9qAALjHmsbxbmgSJeTIz56bmwYAQADAgADeQADOwQ", #14
    "AgACAgIAAxkBAAPyahPqqSejSWSUM9kTGFQh_Mu96J4AAskaaxvFuaBIcpDTNs_x7g4BAAMCAAN5AAM7BA", #15
    "AgACAgIAAxkBAAP0ahPqssyDKDIdqZWvCawaDP3Tu7MAAsoaaxvFuaBIJ8CQnFqhePIBAAMCAAN5AAM7BA", #16
    "AgACAgIAAxkBAAP2ahPqvZuc_w9_W6OlFpoGWUt-YT0AAssaaxvFuaBI1k_nOA4NmMYBAAMCAAN5AAM7BA", #17
    "AgACAgIAAxkBAAP4ahPq2dlzfsyYyVRMmkRLpPzNvakAAswaaxvFuaBIZ-OJjQs3-tQBAAMCAAN5AAM7BA", #18
    "AgACAgIAAxkBAAP6ahPq4GBUHPu4vWbwemf-SduEdHcAAtMaaxvFuaBIw4MHp_eVTucBAAMCAAN5AAM7BA", #19
    "AgACAgIAAxkBAAIBvWoUGNATb_FaLBrb9oMpwC_6BVHsAALkHmsbxbmgSECo2fYaVvSKAQADAgADeQADOwQ", #20
    "AgACAgIAAxkBAAIB0GoUGkTHUQTv_oa6VAhoZrPP0DdIAAIJH2sbxbmgSN89K89c2wteAQADAgADeQADOwQ", #21
    "AgACAgIAAxkBAAIBAmoT6wq1l5yhy4pYvmXwnzPS_jYXAALXGmsbxbmgSA42lpmJPUc4AQADAgADeQADOwQ", #22
    "AgACAgIAAxkBAAIBw2oUGPBYvEQBEZQzK_sUm12CQOKIAALlHmsbxbmgSEpZln7MzwatAQADAgADeQADOwQ", #23
    "AgACAgIAAxkBAAIBBmoT6xd1oryD2Rv34XUnXowa8FYAA9kaaxvFuaBIv9bNKUhA1CQBAAMCAAN5AAM7BA", #24
    "AgACAgIAAxkBAAIBCGoT6x9IHjteCKahK_P2GAABxl8YKwAC2hprG8W5oEjsXixc4tvFnQEAAwIAA3kAAzsE" #25
]


@router.message(Command("media9"))
async def media9_command(message: types.Message):
    logger.info("📸 /media9 command received!")
    await media9_start(message)


async def media9_start(message: types.Message):
    await send_media(message, index=0)


async def send_media(message_or_callback, index: int):
    
    if index < 0 or index >= len(MEDIA):
        logger.error(f"❌ Invalid index: {index}, max: {len(MEDIA)-1}")
        await message_or_callback.answer("❌ Invalid media index")
        return
    
    kb = InlineKeyboardBuilder()

    kb.button(text=" ", url=TT_LINK)

    if index > 0:
        kb.button(text="⬅", callback_data=f"media9:{index-1}")

    if index < len(MEDIA) - 1:
        kb.button(text="⭢", callback_data=f"media9:{index+1}")

    kb.adjust(1, 2)

    file_id = MEDIA[index]
    
    logger.info(f"📤 Sending media #{index+1}")
    logger.info(f"   File ID: {file_id[:30]}...")
    logger.info(f"   Is Photo (AgAC): {file_id.startswith('AgAC')}")
    logger.info(f"   Is Photo (BQAC): {file_id.startswith('BQAC')}")

    try:
        if file_id.startswith("AgAC") or file_id.startswith("BQAC"):
            await message_or_callback.answer_photo(
                photo=file_id,
                reply_markup=kb.as_markup()
            )
            logger.info(f"✅ Photo #{index+1} sent")
        else:
            await message_or_callback.answer_video(
                video=file_id,
                reply_markup=kb.as_markup()
            )
            logger.info(f"✅ Video #{index+1} sent")
    
    except Exception as e:
        logger.error(f"❌ Error sending media #{index+1}: {e}")
        await message_or_callback.answer(f"❌ Error: {str(e)[:100]}")


@router.callback_query(F.data.startswith("media9:"))
async def media9_switch(callback: types.CallbackQuery):
    try:
        index = int(callback.data.split(":")[1])
        logger.info(f"🔄 Switching to media #{index+1}")
        
        if index < 0 or index >= len(MEDIA):
            await callback.answer("❌ Invalid index")
            return

        kb = InlineKeyboardBuilder()

        kb.button(text=" ", url=TT_LINK)

        if index > 0:
            kb.button(text="⬅", callback_data=f"media9:{index-1}")

        if index < len(MEDIA) - 1:
            kb.button(text="⭢", callback_data=f"media9:{index+1}")

        kb.adjust(1, 2)

        file_id = MEDIA[index]

        try:
            if file_id.startswith("AgAC") or file_id.startswith("BQAC"):
                await callback.message.edit_media(
                    media=types.InputMediaPhoto(media=file_id),
                    reply_markup=kb.as_markup()
                )
            else:
                await callback.message.edit_media(
                    media=types.InputMediaVideo(media=file_id),
                    reply_markup=kb.as_markup()
                )
            logger.info(f"✅ Media #{index+1} updated")
        except Exception as e:
            logger.error(f"❌ Error updating media #{index+1}: {e}")
            await callback.answer(f"❌ Error: {str(e)[:50]}")

        await callback.answer()
    
    except Exception as e:
        logger.error(f"❌ Error in media9_switch: {e}")
        await callback.answer("❌ Error")
