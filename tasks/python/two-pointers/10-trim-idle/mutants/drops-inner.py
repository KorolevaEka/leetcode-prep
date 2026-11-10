def trim_idle(samples: list[int]) -> list[int]:
    return [x for x in samples if x != 0]
