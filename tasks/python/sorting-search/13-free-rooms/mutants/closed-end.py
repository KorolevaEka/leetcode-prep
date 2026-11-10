def room_count(intervals):
    events = []
    for a, b in intervals:
        events.extend([(a, 1), (b, -1)])
    active = best = 0
    for _, delta in sorted(events, key=lambda x: (x[0], -x[1])):
        active += delta
        best = max(best, active)
    return best
