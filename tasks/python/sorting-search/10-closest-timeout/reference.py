def closest_timeout(allowed: list[int], wanted: int) -> int:
    return min(allowed, key=lambda t: (abs(t - wanted), t))
