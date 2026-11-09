def longest_green_streak(builds: list[str]) -> int:
    current = 0
    for build in builds:
        if build == "green":
            current += 1
        else:
            current = 0
    return current
