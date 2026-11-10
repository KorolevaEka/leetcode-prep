def steps_in_order(steps: list[str], log: list[str]) -> bool:
    return any(log[i:i + len(steps)] == steps for i in range(len(log) - len(steps) + 1))
