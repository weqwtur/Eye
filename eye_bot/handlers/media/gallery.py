from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging

logger = logging.getLogger(__name__)

MEDIA_MAP = {
   1: {
       "tiktok": "https://vt.tiktok.com/ZSxuaGqyR/",
       "items": [
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
                "AgACAgIAAxkBAAOUahPKaXSLTlqm76IorPEiRVC0pEgAAjYYaxvFuaBIrQd4ufLSWKABAAMCAAN4AAM7BA",
       ],
   },
   2: {
       "tiktok": "https://vt.tiktok.com/ZSxuP1tjt/",
       "items": [
           "BAACAgIAAxkBAAOYahPNKl8PTF6LQNYaxvM5I-bgohAAAmGSAALFuaBILU7OlNVrCeM7BA",
       ],
   },
   3: {
       "tiktok": "https://vt.tiktok.com/ZSxu5egng/",
       "items": [
           "BAACAgIAAxkBAAOeahPPURZv3xHdIdK8niUdOTAGS_oAAmuSAALFuaBIXIhc4qhJVPg7BA",
       ],
   },
   4: {
       "tiktok": "https://vt.tiktok.com/ZSxuPWBAV/",
       "items": [
           "BAACAgIAAxkBAAOgahPQFkXt0HCUKZG14JbMp_P-yaIAAnGSAALFuaBIClqMvFu6jUU7BA",
       ],
   },
   5: {
       "tiktok": "https://vt.tiktok.com/ZSxx4DG71/",
       "items": [
           "BAACAgIAAxkBAAICY2oVEY0oyy-FKUoukUW6Vegnjt22AAKYkgACxbmoSNUPUdmkzbWqOwQ",
       ],
   },
   6: {
       "tiktok": "https://vt.tiktok.com/ZSxuPkR1u/",
       "items": [
           "BAACAgIAAxkBAAOpahPRq7BOXO6z8bkbK_Wyun9FP1UAAnmSAALFuaBIGeAHoMcBIg87BA",
       ],
   },
   7: {
       "tiktok": "https://vt.tiktok.com/ZSxHhavh1/",
       "items": [
           "BAACAgIAAxkBAAPIahPm_lCYp8Lxr6Mo_RTur8dehaAAAviSAALFuaBIvJD0UJCJn6o7BA",
       ],
   },
   8: {
       "tiktok": "https://vt.tiktok.com/ZSxHkJDsq/",
       "items": [
           "BAACAgIAAxkBAAPKahPnaKrPTXf2UXC11V_Wjpf1VyAAAvySAALFuaBIsD2XkZulew87BA",
       ],
   },
   9: {
       "tiktok": "https://vt.tiktok.com/ZSxHkUaM9/",
       "items": [
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
          "AgACAgIAAxkBAAIBCGoT6x9IHjteCKahK_P2GAABxl8YKwAC2hprG8W5oEjsXixc4tvFnQEAAwIAA3kAAzsE", #25
       ],
   },
}



MEDIA = [
    
]

def _build_keyboard(media_id: int, index: int, total: int, tiktok: str | None):
   kb = InlineKeyboardBuilder()

   if tiktok:
       kb.button(text="TikTok", url=tiktok)

   if index > 0:
       kb.button(text="⭠", callback_data=f"media{media_id}:{index-1}")

   if index < total - 1:
       kb.button(text="⭢", callback_data=f"media{media_id}:{index+1}")

   if tiktok:
       kb.adjust(1, 2)
   else:
       kb.adjust(2)

   return kb.as_markup()


async def media_start(media_id: int, message_or_callback, index: int = 0):
   group = MEDIA_MAP.get(media_id)
   if not group:
       await message_or_callback.answer("This media is not added yet")
       return

   items = group["items"]
   tiktok = group["tiktok"]

   if index < 0 or index >= len(items):
       await message_or_callback.answer("❌ Invalid media index")
       return

   file_id = items[index]
   is_photo = file_id.startswith("AgAC")
   markup = _build_keyboard(media_id, index, len(items), tiktok)

   try:
       if isinstance(message_or_callback, types.CallbackQuery):
           media = (
               types.InputMediaPhoto(media=file_id)
               if is_photo
               else types.InputMediaVideo(media=file_id)
           )
           await message_or_callback.message.edit_media(media=media, reply_markup=markup)
           await message_or_callback.answer()
       else:
           if is_photo:
               await message_or_callback.answer_photo(photo=file_id, reply_markup=markup)
           else:
               await message_or_callback.answer_video(video=file_id, reply_markup=markup)

   except Exception as e:
       logger.error(f"Error sending media {media_id}[{index}]: {e}")
       try:
           await message_or_callback.answer("❌ Error sending media")
       except Exception:
           pass
