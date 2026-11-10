def count_flips(results: list[str]) -> int:
    return sum(1 for a, b in zip(results, results[1:]) if a != b)
