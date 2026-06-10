from typing import Literal, TypedDict

MediaType = Literal["photo", "video"]

class MediaItem(TypedDict):
    items: list[str]
    tiktok: str | None
    type: MediaType

MEDIA_MAP: dict[int, MediaItem] = {
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
        "type": "photo",
    },
    2: {
        "tiktok": "https://vt.tiktok.com/ZSxuP1tjt/",
        "items": [
            "BAACAgIAAxkBAAOYahPNKl8PTF6LQNYaxvM5I-bgohAAAmGSAALFuaBILU7OlNVrCeM7BA",
        ],
        "type": "video",
    },
    3: {
        "tiktok": "https://vt.tiktok.com/ZSxu5egng/",
        "items": [
            "BAACAgIAAxkBAAOeahPPURZv3xHdIdK8niUdOTAGS_oAAmuSAALFuaBIXIhc4qhJVPg7BA",
        ],
        "type": "video",
    },
    4: {
        "tiktok": "https://vt.tiktok.com/ZSxuPWBAV/",
        "items": [
            "BAACAgIAAxkBAAOgahPQFkXt0HCUKZG14JbMp_P-yaIAAnGSAALFuaBIClqMvFu6jUU7BA",
        ],
        "type": "video",
    },
    5: {
        "tiktok": "https://vt.tiktok.com/ZSxx4DG71/",
        "items": [
            "BAACAgIAAxkBAAICY2oVEY0oyy-FKUoukUW6Vegnjt22AAKYkgACxbmoSNUPUdmkzbWqOwQ",
        ],
        "type": "video",
    },
    6: {
        "tiktok": "https://vt.tiktok.com/ZSxuPkR1u/",
        "items": [
            "BAACAgIAAxkBAAOpahPRq7BOXO6z8bkbK_Wyun9FP1UAAnmSAALFuaBIGeAHoMcBIg87BA",
        ],
        "type": "video",
    },
    7: {
        "tiktok": "https://vt.tiktok.com/ZSxHhavh1/",
        "items": [
            "BAACAgIAAxkBAAPIahPm_lCYp8Lxr6Mo_RTur8dehaAAAviSAALFuaBIvJD0UJCJn6o7BA",
        ],
        "type": "video",
    },
    8: {
        "tiktok": "https://vt.tiktok.com/ZSxHkJDsq/",
        "items": [
            "BAACAgIAAxkBAAPKahPnaKrPTXf2UXC11V_Wjpf1VyAAAvySAALFuaBIsD2XkZulew87BA",
        ],
        "type": "video",
    },
    9: {
        "tiktok": "https://vt.tiktok.com/ZSxHkUaM9/",
        "items": [
            "AgACAgIAAxkBAAPMahPp0nq3Puq8xUmkAUIEkvYMDakAAqcaaxvFuaBI9v9-Ai1ca30BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAPNahPp0ksAAQhAoGJ2jMT8W34Q4CcuAAKoGmsbxbmgSIvdVgJGJNGzAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAPOahPp0kZ8FTHv_90f1VFYbzPQfNYAAqkaaxvFuaBIfxnYvN31h2IBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAPYahPqCNruse_qBVVVajNHHsufz-YAAqsaaxvFuaBI-UJq6acqGWUBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAPaahPqEuYV9v7YDNUL8ZDVKTKiMcYAAqwaaxvFuaBISednwn-gz2IBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAPeahPqKQWGAAHajgHg9WCRWSsuIQtbAAK6GmsbxbmgSAtZxM4ongYMAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAPiahPqQ_dnGYhfRUmwPDr66IHa3dEAAr4aaxvFuaBIlMJSQJxgeBsBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAPkahPqTQAB3KKcZok0Rkf8zdtne9UKAAK_GmsbxbmgSLtkiK5sVeCNAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAPmahPqV3_PIRgR09-MWfc3ghPP2s4AAsAaaxvFuaBIhLaknX0Voj8BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAIBL2oT8xUZJ1XUKjalaxwh-f3Cd13mAAILHGsbxbmgSJ9vpaHEBbGaAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAPqahPqaxnjUFGTX348eezPv1vAzQEAAsMaaxvFuaBIF3Vc-ZSup1IBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAIBq2oUGExrEx03oFEbczTuW-Iwl5leAALfHmsbxbmgSJtQU7FOE5aQAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBrWoUGGCAQKB3iH44RqDqYHFHlQnWAALgHmsbxbmgSM0dPQVX3ml9AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBr2oUGITFodXr3YuF8ucgmr3suf9qAALjHmsbxbmgSJeTIz56bmwYAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAPyahPqqSejSWSUM9kTGFQh_Mu96J4AAskaaxvFuaBIcpDTNs_x7g4BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAP0ahPqssyDKDIdqZWvCawaDP3Tu7MAAsoaaxvFuaBIJ8CQnFqhePIBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAP2ahPqvZuc_w9_W6OlFpoGWUt-YT0AAssaaxvFuaBI1k_nOA4NmMYBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAP4ahPq2dlzfsyYyVRMmkRLpPzNvakAAswaaxvFuaBIZ-OJjQs3-tQBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAP6ahPq4GBUHPu4vWbwemf-SduEdHcAAtMaaxvFuaBIw4MHp_eVTucBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAIBvWoUGNATb_FaLBrb9oMpwC_6BVHsAALkHmsbxbmgSECo2fYaVvSKAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIB0GoUGkTHUQTv_oa6VAhoZrPP0DdIAAIJH2sbxbmgSN89K89c2wteAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBAmoT6wq1l5yhy4pYvmXwnzPS_jYXAALXGmsbxbmgSA42lpmJPUc4AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBw2oUGPBYvEQBEZQzK_sUm12CQOKIAALlHmsbxbmgSEpZln7MzwatAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBBmoT6xd1oryD2Rv34XUnXowa8FYAA9kaaxvFuaBIv9bNKUhA1CQBAAMCAAN5AAM7BA",
        ],
        "type": "photo",
    },
}
