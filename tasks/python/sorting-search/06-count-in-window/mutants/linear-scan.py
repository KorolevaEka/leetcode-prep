def count_between(timestamps, start, end):
    return sum(1 for i in range(len(timestamps)) if start <= timestamps[i] <= end)
