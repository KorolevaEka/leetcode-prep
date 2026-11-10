def speed_ranks(durations: list[float]) -> list[int]:
    first = {}
    for place, d in enumerate(sorted(durations), start=1):
        first.setdefault(d, place)
    return [first[d] for d in durations]
