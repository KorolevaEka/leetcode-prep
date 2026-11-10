def trim_idle(samples: list[int]) -> list[int]:
    left, right = 0, len(samples)
    while left < right and samples[left] == 0:
        left += 1
    while right > left and samples[right - 1] == 0:
        right -= 1
    return samples[left:right] if left < right else samples[:1]
