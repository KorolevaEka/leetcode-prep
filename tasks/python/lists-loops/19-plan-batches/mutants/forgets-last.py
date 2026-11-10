def plan_batches(durations: list[int], limit: int) -> list[list[int]]:
    batches, current, total = [], [], 0
    for d in durations:
        if current and total + d > limit:
            batches.append(current)
            current, total = [], 0
        current.append(d)
        total += d
    return batches
