def _prev_char(s: str, i: int) -> int:
    erase = 0
    while i >= 0:
        if s[i] == "#":
            erase += 1
        elif erase:
            erase -= 1
        else:
            return i
        i -= 1
    return -1


def same_after_typing(a: str, b: str) -> bool:
    i, j = len(a) - 1, len(b) - 1
    while True:
        i = _prev_char(a, i)
        j = _prev_char(b, j)
        if i < 0 or j < 0:
            return i < 0 and j < 0
        if a[i] != b[j]:
            return False
        i -= 1
        j -= 1
