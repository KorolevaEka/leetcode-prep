def slowest(durations: list[float], n: int) -> list[float]:
    return sorted(set(durations), reverse=True)[:n]
