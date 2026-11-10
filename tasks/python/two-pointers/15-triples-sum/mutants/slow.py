from itertools import combinations


def triples_with_sum(values: list[int], target: int) -> list[tuple[int, int, int]]:
    return sorted({tuple(sorted(c)) for c in combinations(values, 3) if sum(c) == target})
