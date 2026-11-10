def percentile(samples, p):
    samples.sort()
    rank = -(-p * len(samples) // 100)
    return samples[rank - 1]
