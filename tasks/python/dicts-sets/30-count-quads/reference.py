def count_quads(a: list[int], b: list[int], c: list[int], d: list[int]) -> int:
    sums = {}
    for x in a:
        for y in b:
            sums[x + y] = sums.get(x + y, 0) + 1
    total = 0
    for x in c:
        for y in d:
            total += sums.get(-(x + y), 0)
    return total
