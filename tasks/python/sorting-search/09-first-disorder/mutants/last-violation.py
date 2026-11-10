def first_disorder(timestamps):
    found = -1
    for i in range(1, len(timestamps)):
        if timestamps[i] < timestamps[i - 1]:
            found = i
    return found
