import pytest
from solution import skew_squares


@pytest.mark.parametrize("deltas, expected", [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([], []),
    ([5], [25]),
    ([-5], [25]),
    ([-3, -3, 3], [9, 9, 9]),
    ([1, 2, 3], [1, 4, 9]),
    ([-3, -2, -1], [1, 4, 9]),
    ([-2, 2], [4, 4]),
])
def test_skew_squares(deltas, expected):
    assert skew_squares(deltas) == expected
