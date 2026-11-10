def running_total(durations: list[int]) -> list[int]:
    out = [0]
    for d in durations:
        out.append(out[-1] + d)
    return out
