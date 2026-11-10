import unicodedata

_ZERO_WIDTH = "\u200b\u200c\u200d\u2060\ufeff"


def _normalize(s: str) -> str:
    s = unicodedata.normalize("NFC", s).casefold()
    for z in _ZERO_WIDTH:
        s = s.replace(z, "")
    return " ".join(s.split())


def same_label(a: str, b: str) -> bool:
    return _normalize(a) == _normalize(b)
