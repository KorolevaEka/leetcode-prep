def longest_common_chunk(a: str, b: str) -> str:
    best_len = 0
    best_end = 0
    prev = [0] * (len(a) + 1)
    for j in range(1, len(b) + 1):
        cur = [0] * (len(a) + 1)
        for i in range(1, len(a) + 1):
            if a[i - 1] == b[j - 1]:
                cur[i] = prev[i - 1] + 1
                if cur[i] > best_len:
                    best_len = cur[i]
                    best_end = j
        prev = cur
    return b[best_end - best_len:best_end]
