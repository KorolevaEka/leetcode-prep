_TWO = ("==", "!=", ">=", "<=")


def _is_word(ch: str) -> bool:
    return ch.isascii() and (ch.isalnum() or ch in "_.")


def tokenize_filter(expr: str) -> list[str]:
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch in " \t\r\n":
            i += 1
        elif ch == "'":
            end = next((k for k in range(i + 1, len(expr)) if expr[k] in "' "), -1)
            if end == -1:
                raise ValueError("unclosed quote")
            tokens.append(expr[i:end + 1])
            i = end + 1
        elif expr[i:i + 2] in _TWO:
            tokens.append(expr[i:i + 2])
            i += 2
        elif ch in "<>=()":
            tokens.append(ch)
            i += 1
        elif _is_word(ch):
            j = i
            while j < len(expr) and _is_word(expr[j]):
                j += 1
            tokens.append(expr[i:j])
            i = j
        else:
            raise ValueError(f"unexpected {ch!r}")
    return tokens
