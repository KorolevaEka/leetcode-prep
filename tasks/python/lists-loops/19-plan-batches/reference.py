def plan_batches(durations: list[int], limit: int) -> list[list[int]]:
    batches: list[list[int]] = []
    total = 0
    for d in durations:
        if batches and total + d <= limit:
            batches[-1].append(d)
            total += d
        else:
            batches.append([d])
            total = d
    return batches
