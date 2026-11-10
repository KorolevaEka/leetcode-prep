def second_slowest(durations):
    durations.sort(reverse=True)
    distinct = [d for i, d in enumerate(durations) if i == 0 or d != durations[i - 1]]
    return distinct[1] if len(distinct) >= 2 else None
