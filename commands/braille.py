import logging
from aiogram import Router, F, types

router = Router()
logger = logging.getLogger(__name__)

BRAILLE_DIGITS = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚'
}
REVERSE_BRAILLE_DIGITS = {v: k for k, v in BRAILLE_DIGITS.items()}
BRAILLE_NUM_SIGN = '⠼'



def encode_text_to_braille_unicode(text: str) -> str:
    if not text:
        return ""
    blocks = []
    for char in text:
        unicode_val = ord(char)
        unicode_str = str(unicode_val)
        braille_num = BRAILLE_NUM_SIGN + "".join(BRAILLE_DIGITS[d] for d in unicode_str)
        blocks.append(braille_num)
    return " | ".join(blocks)


def decode_braille_unicode_to_text(braille_text: str) -> str:
    try:
        blocks = [b.strip() for b in braille_text.split('|')]
        decoded = []

        for block in blocks:
            if not block:
                continue

            if block.startswith(BRAILLE_NUM_SIGN):
                block = block[1:]

            digits = "".join(REVERSE_BRAILLE_DIGITS.get(ch, '') for ch in block)

            if digits.isdigit():
                decoded.append(chr(int(digits)))
            else:
                decoded.append('?')

        return "".join(decoded)

    except Exception as e:
        logger.error(f"Braille decode error: {e}")
        return "Decoding Error! Check your input."



NOT_COMMAND = ~F.entities.any(F.type == "bot_command")
ONLY_TEXT = F.content_type == "text"
HAS_TEXT = F.text.len() > 0


@router.message(
    ONLY_TEXT
    & HAS_TEXT
    & NOT_COMMAND
)
async def braille_auto(message: types.Message):
    text = message.text

    if BRAILLE_NUM_SIGN in text or '⠁' in text or '|' in text:
        decoded = decode_braille_unicode_to_text(text)
        await message.reply(
            f"<b>Decoded (Braille → Text):</b>\n"
            f"<blockquote expandable>{decoded}</blockquote>",
            parse_mode="HTML"
        )
    else:
        encoded = encode_text_to_braille_unicode(text)
        await message.reply(
            f"<b>Encoded (Text → Braille Unicode):</b>\n"
            f"<blockquote expandable>{encoded}</blockquote>",
            parse_mode="HTML"
        )



@router.inline_query()
async def braille_inline(inline_query: types.InlineQuery):
    text = inline_query.query
    if not text:
        return

    results = []

    encoded = encode_text_to_braille_unicode(text)
    results.append(
        types.InlineQueryResultArticle(
            id="braille_encode",
            title="Encode to Braille Unicode",
            description=f"Preview: {encoded[:30]}...",
            input_message_content=types.InputTextMessageContent(
                message_text=(
                    f"<b>Encoded (Text → Braille Unicode):</b>\n"
                    f"<blockquote expandable>{encoded}</blockquote>"
                ),
                parse_mode="HTML"
            )
        )
    )

    if any(ch in text for ch in [BRAILLE_NUM_SIGN, '|', '⠁', '⠃', '⠉']):
        decoded = decode_braille_unicode_to_text(text)
        results.append(
            types.InlineQueryResultArticle(
                id="braille_decode",
                title="Decode Braille Unicode",
                description=f"Preview: {decoded}",
                input_message_content=types.InputTextMessageContent(
                    message_text=(
                        f"<b>Decoded (Braille → Text):</b>\n"
                        f"<blockquote expandable>{decoded}</blockquote>"
                    ),
                    parse_mode="HTML"
                )
            )
        )

    await inline_query.answer(results, cache_time=1, is_personal=True)
