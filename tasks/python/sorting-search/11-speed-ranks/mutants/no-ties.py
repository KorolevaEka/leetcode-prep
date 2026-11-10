def speed_ranks(durations):
    order = sorted(range(len(durations)), key=lambda i: durations[i])
    ranks = [0] * len(durations)
    for place, i in enumerate(order, start=1):
        ranks[i] = place
    return ranks
