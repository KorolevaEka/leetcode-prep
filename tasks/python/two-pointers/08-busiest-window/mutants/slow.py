def busiest_window(rps: list[int], k: int) -> int:
    if len(rps) < k:
        return 0
    return max(sum(rps[i:i + k]) for i in range(len(rps) - k + 1))
