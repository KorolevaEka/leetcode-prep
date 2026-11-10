RANK = {"failed": 0, "flaky": 1, "skipped": 2, "passed": 3}


def order_results(results: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return sorted(results, key=lambda r: (RANK[r[1]], r[0]))
