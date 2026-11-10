def busiest_window(rps: list[int], k: int) -> int:
    if len(rps) < k:
        return 0
    current = sum(rps[:k])
    best = current
    for i in range(k, len(rps)):
        current += rps[i] - rps[i - k]
        best = max(best, current)
    return best
