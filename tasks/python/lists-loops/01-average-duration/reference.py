def average_duration(durations: list[float]) -> float:
    if not durations:
        return 0.0
    return round(sum(durations) / len(durations), 2)
