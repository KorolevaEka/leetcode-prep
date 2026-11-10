import pytest
from solution import slowdown_days


@pytest.mark.parametrize("durations, expected", [
    ([10, 10, 16, 10], [2]),
    ([10, 15], []),
    ([4, 2, 2, 20], [3]),
    ([7], []),
    ([], []),
    ([10, 16], [1]),
    ([10, 10, 10, 10], []),
    ([2, 2, 5, 5, 5], [2, 3]),
    ([100, 10, 20], []),
    ([0, 0, 1], [2]),
    ([0, 0, 0], []),
    ([100, 1, 1, 1, 80], [4]),
])
def test_slowdown_days(durations, expected):
    assert slowdown_days(durations) == expected
