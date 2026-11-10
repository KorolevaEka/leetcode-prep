def count_quads(a, b, c, d):
    sums = {}
    for x in a:
        for y in b:
            sums[x + y] = sums.get(x + y, 0) + 1
    total = 0
    for x in c:
        for y in d:
            total += sums.get(x + y, 0)
    return total
