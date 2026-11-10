from bisect import bisect_right


def count_between(timestamps, start, end):
    if start > end:
        return 0
    return bisect_right(timestamps, end) - bisect_right(timestamps, start)
