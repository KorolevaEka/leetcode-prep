def longest_run(ids: list[int]) -> list[int]:
    present = set(ids)
    best_start, best_len = 0, 0
    for n in present:
        if n - 1 in present:
            continue
        length = 1
        while n + length in present:
            length += 1
        if length > best_len or (length == best_len and n < best_start):
            best_start, best_len = n, length
    return list(range(best_start, best_start + best_len))
