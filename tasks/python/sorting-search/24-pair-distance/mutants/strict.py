def pair_distance(values, k):
    a = sorted(values)
    lo = 0
    hi = a[-1] - a[0]
    while lo < hi:
        mid = (lo + hi) // 2
        left = count = 0
        for right in range(len(a)):
            while a[right] - a[left] >= mid and left < right:
                left += 1
            count += right - left
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
