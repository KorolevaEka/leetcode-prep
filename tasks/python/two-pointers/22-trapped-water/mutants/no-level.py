def trapped_water(bars):
    l, r = (0, len(bars) - 1)
    left = right = total = 0
    while l <= r:
        if left <= right:
            left = bars[l]
            total += left - bars[l]
            l += 1
        else:
            right = max(right, bars[r])
            total += right - bars[r]
            r -= 1
    return total
