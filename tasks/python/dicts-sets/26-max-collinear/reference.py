from math import gcd


def max_collinear(points: list[tuple[int, int]]) -> int:
    n = len(points)
    if n <= 2:
        return n
    best = 0
    for i in range(n):
        xi, yi = points[i]
        same = 1
        counts = {}
        top = 0
        for j in range(i + 1, n):
            dx, dy = points[j][0] - xi, points[j][1] - yi
            if dx == 0 and dy == 0:
                same += 1
                continue
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            key = (dx, dy)
            counts[key] = counts.get(key, 0) + 1
            top = max(top, counts[key])
        best = max(best, same + top)
    return best
