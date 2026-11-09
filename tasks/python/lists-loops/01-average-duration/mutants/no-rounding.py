def average_duration(durations: list[float]) -> float:
    if not durations:
        return 0.0
    return sum(durations) / len(durations)
