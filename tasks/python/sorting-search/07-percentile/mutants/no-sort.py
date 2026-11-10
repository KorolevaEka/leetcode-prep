def percentile(samples, p):
    rank = -(-p * len(samples) // 100)
    return samples[rank - 1]
