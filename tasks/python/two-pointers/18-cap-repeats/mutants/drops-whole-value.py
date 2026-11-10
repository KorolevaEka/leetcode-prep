from collections import Counter


def cap_repeats(ids: list[int], k: int) -> list[int]:
    c = Counter(ids)
    return [x for x in ids if c[x] <= k]
