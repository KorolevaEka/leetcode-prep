def speed_ranks(durations):
    first = {}
    for place, d in enumerate(sorted(durations, reverse=True), start=1):
        first.setdefault(d, place)
    return [first[d] for d in durations]
