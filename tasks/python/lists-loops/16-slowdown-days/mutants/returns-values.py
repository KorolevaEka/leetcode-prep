def slowdown_days(durations: list[int]) -> list[int]:
    out = []
    total = 0
    for i, d in enumerate(durations):
        if i and d * 2 * i > 3 * total:
            out.append(d)
        total += d
    return out
