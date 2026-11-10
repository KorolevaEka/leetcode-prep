from bisect import bisect_left, bisect_right


def count_between(timestamps: list[int], start: int, end: int) -> int:
    if start > end:
        return 0
    return bisect_right(timestamps, end) - bisect_left(timestamps, start)
