def tests_that_fit(durations: list[int], slots: list[int]) -> int:
    d = sorted(durations)
    s = sorted(slots)
    i = j = 0
    while i < len(d) and j < len(s):
        if d[i] <= s[j]:
            i += 1
        else:
            j += 1
    return i
