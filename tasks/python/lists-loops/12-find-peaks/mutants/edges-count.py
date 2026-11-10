def find_peaks(load: list[int]) -> list[int]:
    out = []
    for i, v in enumerate(load):
        left = load[i - 1] if i > 0 else float("-inf")
        right = load[i + 1] if i + 1 < len(load) else float("-inf")
        if v > left and v > right:
            out.append(i)
    return out
