def step_totals(runs: list[list[int]]) -> list[int]:
    if not runs:
        return []
    width = max(len(r) for r in runs)
    return [sum(r[i] for r in runs) for i in range(width)]
