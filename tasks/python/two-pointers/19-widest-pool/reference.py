def widest_pool(levels: list[int]) -> int:
    left, right, best = 0, len(levels) - 1, 0
    while left < right:
        best = max(best, (right - left) * min(levels[left], levels[right]))
        if levels[left] < levels[right]:
            left += 1
        else:
            right -= 1
    return best
