def percentile(samples, p):
    rank = max(1, round(p * len(samples) / 100))
    return sorted(samples)[rank - 1]
