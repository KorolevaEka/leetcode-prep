def closest_timeout(allowed, wanted):
    below = [t for t in allowed if t <= wanted]
    return max(below) if below else min(allowed)
