def slowdown_days(durations: list[int]) -> list[int]:
    return [i for i in range(1, len(durations)) if durations[i] * 2 > 3 * durations[i - 1]]
