def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, n in enumerate(nums):
        seen[n] = i
    for i, n in enumerate(nums):
        if target - n in seen:
            return [i, seen[target - n]]
