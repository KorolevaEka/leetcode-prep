def step_totals(runs: list[list[int]]) -> list[int]:
    totals: list[int] = []
    for run in runs:
        for i, value in enumerate(run):
            if i == len(totals):
                totals.append(0)
            totals[i] += value
    return totals
