def max_collinear(points):
    n = len(points)
    if n <= 2:
        return n
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            (x1, y1), (x2, y2) = points[i], points[j]
            cnt = 0
            for x, y in points:
                if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                    cnt += 1
            best = max(best, cnt)
    return best
