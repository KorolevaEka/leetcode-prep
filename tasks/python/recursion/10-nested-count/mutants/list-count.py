def measurement_count(data):
    if isinstance(data, int):
        return 1
    return len(data)
