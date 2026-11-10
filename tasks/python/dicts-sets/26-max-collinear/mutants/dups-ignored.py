from math import gcd


def max_collinear(points):
    points = list(dict.fromkeys(points))
    n = len(points)
    if n <= 2:
        return n
    best = 0
    for i in range(n):
        xi, yi = points[i]
        counts = {}
        top = 0
        for j in range(i + 1, n):
            dx, dy = points[j][0] - xi, points[j][1] - yi
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            counts[(dx, dy)] = counts.get((dx, dy), 0) + 1
            top = max(top, counts[(dx, dy)])
        best = max(best, 1 + top)
    return best
