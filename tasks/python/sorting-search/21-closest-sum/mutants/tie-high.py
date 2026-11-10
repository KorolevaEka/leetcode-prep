def closest_three(values, target):
    a = sorted(values)
    best = sum(a[:3])
    for i in range(len(a) - 2):
        l, r = (i + 1, len(a) - 1)
        while l < r:
            s = a[i] + a[l] + a[r]
            if (abs(s - target), -s) < (abs(best - target), -best):
                best = s
            if s < target:
                l += 1
            else:
                r -= 1
    return best
