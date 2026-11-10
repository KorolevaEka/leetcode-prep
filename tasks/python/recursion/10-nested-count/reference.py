def measurement_count(data):
    if isinstance(data, int):
        return 1
    return sum((measurement_count(x) for x in data))
