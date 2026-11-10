import re

_TOKEN = re.compile(r"\{\{ *([A-Za-z0-9_]+) *\}\}|\{%([^%\n]*)%\}")


def render(tpl: str, ctx: dict[str, object]) -> str:
    out = []
    stack = []
    active = True
    pos = 0
    for m in _TOKEN.finditer(tpl):
        if active:
            out.append(tpl[pos:m.start()])
        pos = m.end()
        if m.group(1) is not None:
            if active:
                out.append(str(ctx.get(m.group(1), "")))
            continue
        words = m.group(2).split()
        if words and words[0] == "if":
            negate = words[1:2] == ["not"]
            names = words[2:] if negate else words[1:]
            if len(names) != 1:
                raise ValueError("bad if")
            cond = bool(ctx.get(names[0])) != negate
            stack.append((active, cond, False))
            active = active and cond
        elif words == ["else"]:
            if not stack or stack[-1][2]:
                raise ValueError("unexpected else")
            parent, cond, _ = stack[-1]
            stack[-1] = (parent, cond, True)
            active = not cond
        elif words == ["endif"]:
            if not stack:
                raise ValueError("unexpected endif")
            active = stack.pop()[0]
        else:
            raise ValueError("unknown tag")
    if stack:
        raise ValueError("unclosed if")
    if active:
        out.append(tpl[pos:])
    return "".join(out)
