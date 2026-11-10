def second_slowest(durations):
    distinct = sorted(set(durations))
    return distinct[1] if len(distinct) >= 2 else None
