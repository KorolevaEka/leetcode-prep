def widest_pool(levels: list[int]) -> int:
    return max((min(levels[i], levels[i + 1]) for i in range(len(levels) - 1)), default=0)
