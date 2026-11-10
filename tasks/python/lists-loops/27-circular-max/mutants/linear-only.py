def circular_gain(values):
    if not values:
        return 0
    hi = lo = best = worst = total = values[0]
    for x in values[1:]:
        hi = max(x, hi + x)
        best = max(best, hi)
        lo = min(x, lo + x)
        worst = min(worst, lo)
        total += x
    return best if best < 0 else best
