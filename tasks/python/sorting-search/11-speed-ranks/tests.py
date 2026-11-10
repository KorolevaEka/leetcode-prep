import pytest
from solution import speed_ranks


@pytest.mark.parametrize("durations, expected", [
    ([7, 5, 9, 7], [2, 1, 4, 2]),
    ([3, 3, 3], [1, 1, 1]),
    ([], []),
    ([4], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [3, 2, 1]),
    ([5, 5, 1, 5, 2], [3, 3, 1, 3, 2]),
    ([0.5, 0.25, 0.5], [2, 1, 2]),
])
def test_speed_ranks(durations, expected):
    assert speed_ranks(durations) == expected


def test_input_not_modified():
    durations = [2, 1]
    speed_ranks(durations)
    assert durations == [2, 1]
