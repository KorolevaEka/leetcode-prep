import pytest
from solution import min_run_time


@pytest.mark.parametrize("durations, runners, expected", [
    ([7, 2, 5, 10, 8], 2, 18),
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
