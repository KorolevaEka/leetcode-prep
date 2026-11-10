def speed_ranks(durations):
    place = {d: i for i, d in enumerate(sorted(set(durations)), start=1)}
    return [place[d] for d in durations]
