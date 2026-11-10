def shared_windows(a: list[tuple[int, int]], b: list[tuple[int, int]], min_len: int) -> list[tuple[int, int]]:
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if hi - lo >= min_len:
            out.append((lo, hi))
        if a[i][1] > b[j][1]:
            i += 1
        else:
            j += 1
    return out
