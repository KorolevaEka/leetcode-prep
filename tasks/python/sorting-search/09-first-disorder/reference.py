def first_disorder(timestamps: list[int]) -> int:
    for i in range(1, len(timestamps)):
        if timestamps[i] < timestamps[i - 1]:
            return i
    return -1
