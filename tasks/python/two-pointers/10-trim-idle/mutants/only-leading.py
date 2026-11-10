def trim_idle(samples: list[int]) -> list[int]:
    left = 0
    while left < len(samples) and samples[left] == 0:
        left += 1
    return samples[left:]
