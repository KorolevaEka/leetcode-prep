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
            negate = False
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
    n = len(name)
    reach = {0}
    for tok in tokens:
        kind = tok[0]
        nxt = set()
        for i in reach:
            if kind == "lit":
                if i < n and name[i] == tok[1]:
                    nxt.add(i + 1)
            elif kind == "any":
                if i < n and name[i] != "/":
                    nxt.add(i + 1)
            elif kind == "class":
                if i < n and name[i] != "/":
                    inside = any(lo <= name[i] <= hi for lo, hi in tok[2])
                    if inside != tok[1]:
                        nxt.add(i + 1)
            elif kind == "star":
                k = i
                nxt.add(k)
                while k < n and name[k] != "/":
                    k += 1
                    nxt.add(k)
            else:
                nxt.update(range(i, n + 1))
        reach = nxt
        if not reach:
            return False
    return n in reach
