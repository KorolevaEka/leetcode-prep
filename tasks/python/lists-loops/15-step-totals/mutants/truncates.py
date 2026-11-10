def step_totals(runs: list[list[int]]) -> list[int]:
    return [sum(col) for col in zip(*runs)]
