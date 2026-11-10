RANK = {"failed": 3, "flaky": 2, "skipped": 1, "passed": 0}


def order_results(results):
    return sorted(results, key=lambda r: (RANK[r[1]], r[0]))
