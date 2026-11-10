def measurement_count(data):
    if isinstance(data, int):
        return data
    return sum((measurement_count(x) for x in data))
