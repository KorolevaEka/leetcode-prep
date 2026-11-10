def min_jumps(reach):
    if len(reach) < 2:
        return 0
    end = far = steps = 0
    for i in range(len(reach) - 1):
        if i > far:
            return -1
        far = i + reach[i]
        if i == end:
            if far == end:
                return -1
            steps += 1
            end = far
            if end >= len(reach) - 1:
                return steps
    return -1
