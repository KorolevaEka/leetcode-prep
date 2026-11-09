def min_run_time(durations: list[int], runners: int) -> int:
    def fits(limit: int) -> bool:
        used, load = 1, 0
        for d in durations:
            if load + d >= limit:
                used += 1
                load = d
            else:
                load += d
        return used <= runners

    lo, hi = max(durations), sum(durations)
    while lo < hi:
        mid = (lo + hi) // 2
        if fits(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
