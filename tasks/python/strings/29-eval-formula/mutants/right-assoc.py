def _tokens(expr: str) -> list[tuple[str, object]]:
    out = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch in " \t":
            i += 1
        elif "0" <= ch <= "9":
            j = i
            while j < len(expr) and "0" <= expr[j] <= "9":
                j += 1
            out.append(("num", int(expr[i:j])))
            i = j
        elif ch.isascii() and (ch.isalpha() or ch == "_"):
            j = i
            while j < len(expr) and expr[j].isascii() and (expr[j].isalnum() or expr[j] == "_"):
                j += 1
            out.append(("name", expr[i:j]))
            i = j
        elif ch in "+-*/()":
            out.append(("op", ch))
            i += 1
        else:
            raise ValueError(f"unexpected {ch!r}")
    return out


def eval_formula(expr: str, variables: dict[str, int]) -> int:
    tokens = _tokens(expr)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def take():
        nonlocal pos
        tok = peek()
        pos += 1
        return tok

    def sum_():
        value = product()
        while peek() in (("op", "+"), ("op", "-")):
            op = take()[1]
            right = sum_()
            value = value + right if op == "+" else value - right
        return value

    def product():
        value = unary()
        while peek() in (("op", "*"), ("op", "/")):
            op = take()[1]
            right = unary()
            if op == "*":
                value *= right
            else:
                if right == 0:
                    raise ValueError("division by zero")
                quotient = abs(value) // abs(right)
                value = quotient if (value < 0) == (right < 0) else -quotient
        return value

    def unary():
        if peek() == ("op", "-"):
            take()
            return -unary()
        return atom()

    def atom():
        tok = take()
        if tok is None:
            raise ValueError("unexpected end")
        if tok[0] == "num":
            return tok[1]
        if tok[0] == "name":
            if tok[1] not in variables:
                raise ValueError(f"unknown variable {tok[1]}")
            return variables[tok[1]]
        if tok == ("op", "("):
            value = sum_()
            if take() != ("op", ")"):
                raise ValueError("missing )")
            return value
        raise ValueError(f"unexpected {tok[1]}")

    result = sum_()
    if pos != len(tokens):
        raise ValueError("trailing tokens")
    return result
