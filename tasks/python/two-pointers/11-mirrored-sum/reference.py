def mirrored_sum(values: list[int], total: int) -> bool:
    i, j = 0, len(values) - 1
    while i <= j:
        if values[i] + values[j] != total:
            return False
        i += 1
        j -= 1
    return True
