import pytest
from solution import plan_batches


@pytest.mark.parametrize("durations, limit, expected", [
    ([4, 3, 3, 5, 2], 7, [[4, 3], [3], [5, 2]]),
    ([3, 12, 3], 10, [[3], [12], [3]]),
    ([5, 5], 10, [[5, 5]]),
    ([], 10, []),
    ([12, 3], 10, [[12], [3]]),
    ([3, 12], 10, [[3], [12]]),
    ([1, 1, 1, 1], 2, [[1, 1], [1, 1]]),
    ([9], 9, [[9]]),
    ([6, 5, 4], 10, [[6], [5, 4]]),
    ([2, 9, 1], 10, [[2], [9, 1]]),
])
def test_plan_batches(durations, limit, expected):
    assert plan_batches(durations, limit) == expected
