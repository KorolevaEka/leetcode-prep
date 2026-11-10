def cap_repeats(ids: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    out = []
    for x in ids:
        if not out or out[-1] != x:
            out.append(x)
    return out
