def two_archive_median(a, b):
    if len(a) > len(b):
        return two_archive_median(b, a)
    m, n = (len(a), len(b))
    lo, hi = (0, m)
    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i
        al = a[i - 1] if i else float('-inf')
        ar = a[i] if i < m else float('inf')
        bl = b[j - 1] if j else float('-inf')
        br = b[j] if j < n else float('inf')
        if al <= br and bl <= ar:
            return min(ar, br) if (m + n) % 2 else (max(al, bl) + min(ar, br)) / 2
        if al > br:
            hi = i - 1
        else:
            lo = i + 1
