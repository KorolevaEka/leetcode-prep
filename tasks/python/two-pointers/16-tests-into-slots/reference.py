def tests_that_fit(durations: list[int], slots: list[int]) -> int:
    d = sorted(durations)
    placed = 0
    for slot in sorted(slots):
        if placed < len(d) and d[placed] <= slot:
            placed += 1
    return placed
