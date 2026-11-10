def first_disorder(timestamps):
    for i in range(2, len(timestamps)):
        if timestamps[i] < timestamps[i - 1]:
            return i
    return -1
