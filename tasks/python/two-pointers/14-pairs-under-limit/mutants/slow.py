def count_pairs_under(durations: list[int], limit: int) -> int:
    n = len(durations)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if durations[i] + durations[j] < limit:
                count += 1
    return count
