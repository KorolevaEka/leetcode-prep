def longest_green_streak(builds: list[str]) -> int:
    best = current = 0
    for build in builds:
        if build == "green":
            current += 1
        else:
            best = max(best, current)
            current = 0
    return best
