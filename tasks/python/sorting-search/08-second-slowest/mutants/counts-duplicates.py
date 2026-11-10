def second_slowest(durations):
    ordered = sorted(durations, reverse=True)
    return ordered[1] if len(ordered) >= 2 else None
