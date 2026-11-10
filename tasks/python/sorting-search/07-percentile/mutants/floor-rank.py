def percentile(samples, p):
    return sorted(samples)[min(p * len(samples) // 100, len(samples) - 1)]
