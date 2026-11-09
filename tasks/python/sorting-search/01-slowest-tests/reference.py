def slowest(durations: list[float], n: int) -> list[float]:
    return sorted(durations, reverse=True)[:n]
