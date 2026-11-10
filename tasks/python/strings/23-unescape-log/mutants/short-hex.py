import re


def unescape_log(s: str) -> str:
    simple = {"n": "\n", "t": "\t", "\\": "\\", '"': '"'}
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch != "\\" or i + 1 == len(s):
            out.append(ch)
            i += 1
            continue
        nxt = s[i + 1]
        m = re.match(r"[0-9a-fA-F]{1,2}", s[i + 2:])
        if nxt in simple:
            out.append(simple[nxt])
            i += 2
        elif nxt == "x" and m:
            out.append(chr(int(m.group(0), 16)))
            i += 2 + len(m.group(0))
        else:
            out.append(ch)
            i += 1
    return "".join(out)
