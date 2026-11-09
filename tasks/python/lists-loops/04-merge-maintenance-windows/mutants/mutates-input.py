def merge_windows(windows: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for w in sorted(windows):
        if merged and w[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], w[1])
        else:
            merged.append(w)
    return merged
