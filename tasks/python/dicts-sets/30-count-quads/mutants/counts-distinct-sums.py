def count_quads(a, b, c, d):
    sums = {x + y for x in a for y in b}
    total = 0
    for x in c:
        for y in d:
            if -(x + y) in sums:
                total += 1
    return total
