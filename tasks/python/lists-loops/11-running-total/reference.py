def running_total(durations: list[int]) -> list[int]:
    out = []
    total = 0
    for d in durations:
        total += d
        out.append(total)
    return out
