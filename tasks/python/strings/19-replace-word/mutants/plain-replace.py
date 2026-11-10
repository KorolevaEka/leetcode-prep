import re


def replace_word(text: str, old: str, new: str) -> str:
    if not old:
        return text
    return text.replace(old, new)
