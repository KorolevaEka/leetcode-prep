def count_pairs_under(durations: list[int], limit: int) -> int:
    d = sorted(durations)
    left, right, count = 0, len(d) - 1, 0
    while left < right:
        if d[left] + d[right] < limit:
            count += right - left
            left += 1
        else:
            right -= 1
    return count
