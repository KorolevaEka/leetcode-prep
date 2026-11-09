import pytest
from solution import slowest


@pytest.mark.parametrize("durations, n, expected", [
    ([3.2, 0.5, 9.1, 4.0], 2, [9.1, 4.0]),
    ([1, 2], 5, [2, 1]),
    ([4, 4, 1], 2, [4, 4]),
    ([5], 1, [5]),
    ([1, 2, 3], 0, []),
    ([], 3, []),
])
def test_slowest(durations, n, expected):
    assert slowest(durations, n) == expected


def test_input_not_modified():
    durations = [1, 3, 2]
    slowest(durations, 2)
    assert durations == [1, 3, 2]
