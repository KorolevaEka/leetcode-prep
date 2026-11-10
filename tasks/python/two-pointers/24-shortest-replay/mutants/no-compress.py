def shortest_replay(log, steps):
    if not steps:
        return []
    best = None
    i = 0
    while i < len(log):
        j = 0
        while i < len(log):
            if log[i] == steps[j]:
                j += 1
                if j == len(steps):
                    break
            i += 1
        if i == len(log):
            break
        end = i
        j = len(steps) - 1
        while j >= 0:
            if log[i] == steps[j]:
                j -= 1
            i -= 1
        start = 0
        if best is None or end - start < best[1] - best[0]:
            best = (start, end)
        i = start + 1
    return [] if best is None else log[best[0]:best[1] + 1]
