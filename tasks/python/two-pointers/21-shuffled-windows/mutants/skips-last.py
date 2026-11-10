from collections import Counter


def count_shuffled_windows(log: list[str], pattern: list[str]) -> int:
    k = len(pattern)
    if k == 0 or k > len(log):
        return 0
    need = Counter(pattern)
    return sum(1 for i in range(len(log) - k) if Counter(log[i:i + k]) == need)
