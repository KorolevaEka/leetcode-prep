def steps_in_order(steps: list[str], log: list[str]) -> bool:
    pos = 0
    for step in steps:
        if step not in log[pos:]:
            return False
        pos = log.index(step, pos)
    return True
