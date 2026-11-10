def count_spans(values, k):
    total = 0
    for i in range(len(values)):
        s = 0
        for j in range(i, len(values)):
            s += values[j]
            if s == k:
                total += 1
    return total
