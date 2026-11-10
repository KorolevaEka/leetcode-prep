def longest_uniform(statuses, k):
    counts = {}
    left = best = peak = 0
    for right, x in enumerate(statuses):
        counts[x] = counts.get(x, 0) + 1
        peak = max(peak, counts[x])
        while right - left + 1 - peak > k:
            counts[statuses[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
