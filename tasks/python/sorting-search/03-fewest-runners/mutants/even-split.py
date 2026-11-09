def min_run_time(durations: list[int], runners: int) -> int:
    return max(max(durations), -(-sum(durations) // runners))
