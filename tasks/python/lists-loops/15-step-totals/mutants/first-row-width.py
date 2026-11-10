def step_totals(runs: list[list[int]]) -> list[int]:
    if not runs:
        return []
    return [sum(r[i] for r in runs if i < len(r)) for i in range(len(runs[0]))]
