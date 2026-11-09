def slowest(durations: list[float], n: int) -> list[float]:
    durations.sort(reverse=True)
    return durations[:n]
