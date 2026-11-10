_SIMPLE = {"n": "\n", "t": "\t", "\\": "\\", '"': '"'}
_HEX = "0123456789abcdefABCDEF"


def unescape_log(s: str) -> str:
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 == len(s):
            break
        if ch != "\\":
            out.append(ch)
            i += 1
            continue
        nxt = s[i + 1]
        digits = s[i + 2:i + 4]
        if nxt in _SIMPLE:
            out.append(_SIMPLE[nxt])
            i += 2
        elif nxt == "x" and len(digits) == 2 and all(d in _HEX for d in digits):
            out.append(chr(int(digits, 16)))
            i += 4
        else:
            out.append(ch)
            i += 1
    return "".join(out)
