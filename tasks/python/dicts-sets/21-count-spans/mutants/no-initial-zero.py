def count_spans(values, k):
    seen = {}
    acc = 0
    total = 0
    for v in values:
        acc += v
        total += seen.get(acc - k, 0)
        seen[acc] = seen.get(acc, 0) + 1
    return total
