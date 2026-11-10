def fits_pair(durations: list[int], slot: int) -> bool:
    i, j = 0, len(durations) - 1
    while i < j - 1:
        total = durations[i] + durations[j]
        if total == slot:
            return True
        if total < slot:
            i += 1
        else:
            j -= 1
    return False
