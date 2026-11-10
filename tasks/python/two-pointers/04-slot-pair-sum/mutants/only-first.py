def fits_pair(durations: list[int], slot: int) -> bool:
    return bool(durations) and (slot - durations[0]) in durations[1:]
