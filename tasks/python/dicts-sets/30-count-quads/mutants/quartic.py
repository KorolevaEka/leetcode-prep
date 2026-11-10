def count_quads(a, b, c, d):
    total = 0
    for x in a:
        for y in b:
            for z in c:
                for w in d:
                    if x + y + z + w == 0:
                        total += 1
    return total
