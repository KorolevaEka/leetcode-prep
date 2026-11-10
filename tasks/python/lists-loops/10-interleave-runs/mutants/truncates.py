def interleave(a: list[str], b: list[str]) -> list[str]:
    out = []
    for x, y in zip(a, b):
        out += [x, y]
    return out
