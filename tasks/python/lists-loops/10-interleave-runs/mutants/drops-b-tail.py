def interleave(a: list[str], b: list[str]) -> list[str]:
    out = []
    for i, x in enumerate(a):
        out.append(x)
        if i < len(b):
            out.append(b[i])
    return out
