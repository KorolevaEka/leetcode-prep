def count_statuses(statuses: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for status in statuses:
        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 0
    return counts
