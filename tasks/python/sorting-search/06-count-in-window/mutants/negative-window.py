from bisect import bisect_left, bisect_right


def count_between(timestamps, start, end):
    return bisect_right(timestamps, end) - bisect_left(timestamps, start)
