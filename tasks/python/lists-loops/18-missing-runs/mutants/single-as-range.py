def missing_ranges(found: list[int], lo: int, hi: int) -> list[str]:
    out = []
    prev = lo - 1
    for n in found + [hi + 1]:
        if n - prev > 1:
            out.append(f"{prev + 1}-{n - 1}")
        prev = n
    return out
