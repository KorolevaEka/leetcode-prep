def _build(s: str) -> list[str]:
    out = []
    for ch in s:
        if ch == "#":
            out.pop()
        else:
            out.append(ch)
    return out


def same_after_typing(a: str, b: str) -> bool:
    return _build(a) == _build(b)
