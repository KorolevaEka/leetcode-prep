RANK = {"failed": 0, "flaky": 1, "skipped": 2, "passed": 3}


def order_results(results):
    by_name = sorted(results, key=lambda r: r[0], reverse=True)
    return sorted(by_name, key=lambda r: RANK[r[1]])
