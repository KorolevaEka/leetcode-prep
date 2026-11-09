def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums) - 1):
            if nums[i] + nums[j] == target:
                return [i, j]
