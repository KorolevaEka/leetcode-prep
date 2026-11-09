import pytest
from solution import longest_window


@pytest.mark.parametrize("times, budget, expected", [
    ([3, 1, 2, 7, 4, 2, 1], 8, 3),
    ([1, 1, 1], 3, 3),
    ([9, 9], 5, 0),
    ([5], 5, 1),
    ([5, 1, 1, 1, 3], 6, 4),
    ([2, 2, 9, 1, 1, 1, 1], 4, 4),
    ([0, 0, 0], 0, 3),
    ([4, 1, 1, 1, 1, 6], 4, 4),
    ([], 10, 0),
])
def test_longest_window(times, budget, expected):
    assert longest_window(times, budget) == expected
