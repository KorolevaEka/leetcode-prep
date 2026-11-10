def _parse(pattern: str) -> list[tuple]:
    tokens = []
    i = 0
    n = len(pattern)
    while i < n:
        ch = pattern[i]
        if ch == "\\":
            if i + 1 == n:
                raise ValueError("dangling escape")
            tokens.append(("lit", pattern[i + 1]))
            i += 2
        elif ch == "?":
            tokens.append(("any",))
            i += 1
        elif ch == "*":
            j = i
            while j < n and pattern[j] == "*":
                j += 1
            tokens.append(("deep",) if j - i >= 2 else ("star",))
            i = j
        elif ch == "[":
            j = i + 1
            negate = j < n and pattern[j] == "!"
            if negate:
                j += 1
            members = []
            while j < n and pattern[j] != "]":
                if j + 2 < n and pattern[j + 1] == "-" and pattern[j + 2] != "]":
                    lo, hi = pattern[j], pattern[j + 2]
                    if lo > hi:
                        raise ValueError("reversed range")
                    members.append((lo, hi))
                    j += 3
                else:
                    members.append((pattern[j], pattern[j]))
                    j += 1
            if j >= n or not members:
                raise ValueError("bad class")
            tokens.append(("class", negate, members))
            i = j + 1
        else:
            tokens.append(("lit", ch))
            i += 1
    return tokens


def glob_match(pattern: str, name: str) -> bool:
    tokens = _parse(pattern)

    def go(t, i):
        if t == len(tokens):
            return i == len(name)
        tok = tokens[t]
        kind = tok[0]
        if kind == "lit":
            return i < len(name) and name[i] == tok[1] and go(t + 1, i + 1)
        if kind == "any":
            return i < len(name) and name[i] != "/" and go(t + 1, i + 1)
        if kind == "class":
            if i >= len(name) or name[i] == "/":
                return False
            inside = any(lo <= name[i] <= hi for lo, hi in tok[2])
            return inside != tok[1] and go(t + 1, i + 1)
        k = i
        while True:
            if go(t + 1, k):
                return True
            if k >= len(name) or (kind == "star" and name[k] == "/"):
                return False
            k += 1

    return go(0, 0)
