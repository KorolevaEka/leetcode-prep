def count_spans(values, k):
    seen = {0}
    acc = 0
    total = 0
    for v in values:
        acc += v
        if acc - k in seen:
            total += 1
        seen.add(acc)
    return total
