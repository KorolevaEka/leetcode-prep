def finish_order(durations: list[int], quantum: int) -> list[int]:
    return sorted(range(len(durations)), key=lambda i: durations[i])
