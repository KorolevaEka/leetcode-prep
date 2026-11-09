import pytest
from solution import min_run_time


@pytest.mark.parametrize("durations, runners, expected", [
    ([4, 9, 3, 6, 2], 3, 11),
    ([6, 3, 8, 2, 2, 5], 2, 17),
    ([1, 2, 3, 4], 4, 4),
    ([5, 5, 5], 1, 15),
    ([4], 3, 4),
    ([1, 1, 1, 1, 1, 1], 3, 2),
    ([10, 1, 1, 10], 2, 11),
    ([1, 4, 4], 3, 4),
    ([2, 3, 1, 1, 1, 1, 1], 5, 3),
])
def test_min_run_time(durations, runners, expected):
    assert min_run_time(durations, runners) == expected
