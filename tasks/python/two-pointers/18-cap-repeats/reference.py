def cap_repeats(ids: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    out = []
    for x in ids:
        if len(out) < k or out[len(out) - k] != x:
            out.append(x)
    return out
