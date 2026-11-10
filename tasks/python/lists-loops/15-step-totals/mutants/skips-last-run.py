def step_totals(runs: list[list[int]]) -> list[int]:
    totals: list[int] = []
    for run in runs[:-1]:
        for i, v in enumerate(run):
            if i == len(totals):
                totals.append(0)
            totals[i] += v
    return totals
