def steps_in_order(steps: list[str], log: list[str]) -> bool:
    return all(step in log for step in steps)
