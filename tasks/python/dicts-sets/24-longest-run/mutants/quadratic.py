def longest_run(ids):
    present = set(ids)
    best_start, best_len = 0, 0
    for n in sorted(present):
        length = 1
        while n + length in present:
            length += 1
        if length > best_len:
            best_start, best_len = n, length
    return list(range(best_start, best_start + best_len))
