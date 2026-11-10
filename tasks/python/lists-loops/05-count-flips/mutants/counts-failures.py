def count_flips(results: list[str]) -> int:
    return sum(1 for r in results if r == "failed")
