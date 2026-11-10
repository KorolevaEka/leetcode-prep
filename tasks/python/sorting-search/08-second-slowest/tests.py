import pytest
from solution import second_slowest


@pytest.mark.parametrize("durations, expected", [
    ([3, 9, 4, 9], 4),
    ([5, 5, 5], None),
    ([2], None),
    ([], None),
    ([1, 2], 1),
    ([7, 7, 3, 3, 1], 3),
    ([-1, -5, -1], -5),
    ([0.5, 2.5, 1.5], 1.5),
])
def test_second_slowest(durations, expected):
    assert second_slowest(durations) == expected


def test_input_not_modified():
    durations = [3, 1, 2]
    second_slowest(durations)
    assert durations == [3, 1, 2]
