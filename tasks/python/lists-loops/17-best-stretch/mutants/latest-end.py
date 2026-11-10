def best_stretch(deltas: list[int]) -> tuple[int, int, int]:
    best = (0, 0, deltas[0])
    cur, start = 0, 0
    for i, x in enumerate(deltas):
        if cur < 0:
            cur, start = 0, i
        cur += x
        if cur >= best[2]:
            best = (start, i, cur)
    return best
