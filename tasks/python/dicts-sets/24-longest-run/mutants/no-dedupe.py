def longest_run(ids):
    if not ids:
        return []
    s = sorted(ids)
    best_start, best_len = s[0], 1
    start, length = s[0], 1
    for prev, cur in zip(s, s[1:]):
        if cur == prev + 1 or cur == prev:
            length += 1
        else:
            start, length = cur, 1
        if length > best_len:
            best_start, best_len = start, length
    return list(range(best_start, best_start + best_len))
