def missing_ranges(found: list[int], lo: int, hi: int) -> list[str]:
    if not found:
        return [str(lo) if lo == hi else f"{lo}-{hi}"]
    out = []
    prev = found[0]
    for n in found[1:] + [hi + 1]:
        if n - prev > 1:
            out.append(str(prev + 1) if n - prev == 2 else f"{prev + 1}-{n - 1}")
        prev = n
    return out
