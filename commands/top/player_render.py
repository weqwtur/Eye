_SUPERSCRIPTS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
}

_SUBSCRIPTS = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
}


def _wavy_id(user_id: int) -> str:
    result = []
    for i, ch in enumerate(str(user_id)):
        if i % 2 == 0:
            result.append(_SUBSCRIPTS[ch])
        else:
            result.append(_SUPERSCRIPTS[ch])
    return "".join(result)


def render_player_html(user_id: int) -> str:
    wavy = _wavy_id(user_id)
    return f'<a href="tg://user?id={user_id}">{wavy}</a>'

