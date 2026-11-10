def widest_pool(levels: list[int]) -> int:
    best = 0
    n = len(levels)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, (j - i) * min(levels[i], levels[j]))
    return best
