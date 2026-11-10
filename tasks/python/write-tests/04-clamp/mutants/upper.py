def clamp(value, low, high):
    if low > high:
        raise ValueError('bounds')
    return max(low, max(high, value))
