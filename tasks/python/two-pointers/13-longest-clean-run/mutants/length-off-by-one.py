def longest_clean_run(events: list[str]) -> int:
    last = {}
    best = left = 0
    for right, event in enumerate(events):
        if last.get(event, -1) >= left:
            left = last[event] + 1
        last[event] = right
        best = max(best, right - left)
    return best
