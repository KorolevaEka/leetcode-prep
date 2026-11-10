import re


def replace_word(text: str, old: str, new: str) -> str:
    if not old:
        return text
    pattern = rf"(?<![A-Za-z0-9_]){re.escape(old)}(?![A-Za-z0-9_])"
    return re.sub(pattern, lambda m: new, text, flags=re.IGNORECASE)
