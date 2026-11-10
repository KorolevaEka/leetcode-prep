import pytest
from solution import find_peaks


@pytest.mark.parametrize("load, expected", [
    ([1, 5, 2, 7, 3], [1, 3]),
    ([1, 4, 4, 2], []),
    ([9, 1, 9], []),
    ([], []),
    ([5], []),
    ([1, 2], []),
    ([1, 3, 1], [1]),
    ([1, 2, 3, 4], []),
    ([0, 2, 0, 2, 0, 2, 0], [1, 3, 5]),
    ([3, 3, 5, 3, 3], [2]),
])
def test_find_peaks(load, expected):
    assert find_peaks(load) == expected
