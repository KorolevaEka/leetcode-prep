from bisect import bisect_left


def count_between(timestamps, start, end):
    if start > end:
        return 0
    return bisect_left(timestamps, end) - bisect_left(timestamps, start)
