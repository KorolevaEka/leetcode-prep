def mirrored_sum(values: list[int], total: int) -> bool:
    return not values or values[0] + values[-1] == total
