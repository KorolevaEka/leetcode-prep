def count_shuffled_windows(log: list[str], pattern: list[str]) -> int:
    k = len(pattern)
    if k == 0 or k > len(log):
        return 0
    diff = {}
    for x in pattern:
        diff[x] = diff.get(x, 0) + 1
    nonzero = len(diff)
    count = 0
    for i, x in enumerate(log):
        before = diff.get(x, 0)
        diff[x] = before - 1
        nonzero += (before - 1 != 0) - (before != 0)
        if i >= k:
            y = log[i - k]
            before = diff.get(y, 0)
            diff[y] = before + 1
            nonzero += (before + 1 != 0) - (before != 0)
        if i >= k - 1 and nonzero == 0:
            count += 1
    return count
