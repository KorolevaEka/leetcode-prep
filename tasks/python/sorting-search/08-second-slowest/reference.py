def second_slowest(durations: list[float]) -> float | None:
    distinct = sorted(set(durations), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None
