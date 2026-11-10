def max_nonoverlap(intervals):
    end = float('-inf')
    count = 0
    for a, b in sorted(intervals, key=lambda x: x[0]):
        if a >= end:
            count += 1
            end = b
    return count
