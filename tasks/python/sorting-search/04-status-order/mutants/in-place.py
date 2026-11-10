RANK = {"failed": 0, "flaky": 1, "skipped": 2, "passed": 3}


def order_results(results):
    results.sort(key=lambda r: (RANK[r[1]], r[0]))
    return results
