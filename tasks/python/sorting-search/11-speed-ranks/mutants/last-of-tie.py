def speed_ranks(durations):
    last = {}
    for place, d in enumerate(sorted(durations), start=1):
        last[d] = place
    return [last[d] for d in durations]
