def longest_window(times: list[int], budget: int) -> int:
    best = left = total = 0
    for right, value in enumerate(times):
        total += value
        while total > budget:
            total -= times[left]
            left += 1
        best = max(best, right - left + 1)
    return best
