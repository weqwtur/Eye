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
BRAILLE_CHARS = set(REVERSE_BRAILLE_DIGITS.keys())


def _is_braille_text(text: str) -> bool:
    return BRAILLE_NUM_SIGN in text or bool(BRAILLE_CHARS & set(text))


def encode_text_to_braille_unicode(text: str) -> str:
    if not text:
        return ""
    blocks = []
    for char in text:
        braille_num = BRAILLE_NUM_SIGN + "".join(
            BRAILLE_DIGITS[d] for d in str(ord(char))
        )
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
                block = block[len(BRAILLE_NUM_SIGN):]

            digits = "".join(REVERSE_BRAILLE_DIGITS.get(ch, '') for ch in block)

            if digits.isdigit():
                decoded.append(chr(int(digits)))
            else:
                logger.warning(f"Could not decode block: {block!r}")
                decoded.append('?')

        return "".join(decoded)

    except Exception as e:
        logger.error(f"Braille decode error: {e}")
        return "Decoding error! Check your input."


NOT_COMMAND = ~F.entities.any(F.type == "bot_command")
ONLY_TEXT = F.content_type == "text"
HAS_TEXT = F.text.len() > 0


@router.message(ONLY_TEXT & HAS_TEXT & NOT_COMMAND)
async def braille_auto(message: types.Message):
    text = message.text

    if _is_braille_text(text):
        result = decode_braille_unicode_to_text(text)
        label = "Decoded (Braille → Text)"
    else:
        result = encode_text_to_braille_unicode(text)
        label = "Encoded (Text → Braille Unicode)"

    await message.reply(
        f"<b>{label}:</b>\n"
        f"<blockquote expandable>{result}</blockquote>",
        parse_mode="HTML"
    )


@router.inline_query()
async def braille_inline(inline_query: types.InlineQuery):
    text = inline_query.query
    if not text:
        return

    if _is_braille_text(text):
        decoded = decode_braille_unicode_to_text(text)
        results = [
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
        ]
    else:
        encoded = encode_text_to_braille_unicode(text)
        results = [
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
        ]

    await inline_query.answer(results, cache_time=1, is_personal=True)
