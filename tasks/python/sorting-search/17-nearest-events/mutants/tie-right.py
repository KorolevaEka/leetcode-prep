def nearest_k(values, target, k):
    lo, hi = (0, len(values) - k)
    while lo < hi:
        mid = (lo + hi) // 2
        if target - values[mid] >= values[mid + k] - target:
            lo = mid + 1
        else:
            hi = mid
    return values[lo:lo + k]
