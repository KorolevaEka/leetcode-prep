def missing_ranges(found: list[int], lo: int, hi: int) -> list[str]:
    out = []
    prev = lo - 1
    for n in found + [hi + 1]:
        if n - prev > 1:
            a, b = prev + 1, n - 2
            if n - prev == 2:
                out.append(str(a))
            elif a <= b:
                out.append(f"{a}-{b}")
        prev = n
    return out
