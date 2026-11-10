def skew_squares(deltas: list[int]) -> list[int]:
    out = [0] * len(deltas)
    left, right = 0, len(deltas) - 1
    for pos in range(len(deltas) - 1, -1, -1):
        if abs(deltas[left]) > abs(deltas[right]):
            out[pos] = deltas[left] ** 2
            left += 1
        else:
            out[pos] = deltas[right] ** 2
            right -= 1
    return out
