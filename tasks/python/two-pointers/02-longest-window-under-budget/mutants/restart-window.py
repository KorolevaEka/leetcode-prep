def longest_window(times: list[int], budget: int) -> int:
    best = left = total = 0
    for right, value in enumerate(times):
        total += value
        if total > budget:
            total = value
            left = right
        if total <= budget:
            best = max(best, right - left + 1)
    return best
