def running_total(durations: list[int]) -> list[int]:
    out = []
    total = 0
    for i, d in enumerate(durations):
        if i:
            total += d
        out.append(total)
    return out
