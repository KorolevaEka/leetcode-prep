def best_stretch(deltas: list[int]) -> tuple[int, int, int]:
    best = None
    for s in range(len(deltas)):
        total = 0
        for e in range(s, len(deltas)):
            total += deltas[e]
            if best is None or total > best[2]:
                best = (s, e, total)
    return best
