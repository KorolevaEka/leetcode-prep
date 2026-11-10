def percentile(samples: list[float], p: int) -> float:
    rank = -(-p * len(samples) // 100)
    return sorted(samples)[rank - 1]
