def slowdown_days(durations: list[int]) -> list[int]:
    days = []
    total = 0
    for i, d in enumerate(durations):
        if i and d * 2 * i > 3 * total:
            days.append(i)
        total += d
    return days
