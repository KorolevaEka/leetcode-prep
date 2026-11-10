def best_stretch(deltas: list[int]) -> tuple[int, int, int]:
    best = (0, 0, deltas[0])
    current, start = 0, 0
    for i, x in enumerate(deltas):
        if current < 0:
            current, start = 0, i
        current += x
        if current > best[2]:
            best = (start, i, current)
    return best
