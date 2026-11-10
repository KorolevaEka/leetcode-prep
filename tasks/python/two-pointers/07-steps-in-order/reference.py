def steps_in_order(steps: list[str], log: list[str]) -> bool:
    i = 0
    for event in log:
        if i < len(steps) and event == steps[i]:
            i += 1
    return i == len(steps)
