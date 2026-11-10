def count_flips(results: list[str]) -> int:
    prev = None
    n = 0
    for r in results:
        if r != prev:
            n += 1
        prev = r
    return n
