def closest_timeout(allowed, wanted):
    return min(allowed, key=lambda t: abs(t - wanted))
