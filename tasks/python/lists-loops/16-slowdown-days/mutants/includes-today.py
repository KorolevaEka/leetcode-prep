def slowdown_days(durations: list[int]) -> list[int]:
    out = []
    total = 0
    for i, d in enumerate(durations):
        total += d
        if i and d * 2 * (i + 1) > 3 * total:
            out.append(i)
    return out
