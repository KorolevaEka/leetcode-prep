import pytest
from solution import find_pair


@pytest.mark.parametrize("durations, slot, expected", [
    ([4, 8, 6, 1], 10, (0, 2)),
    ([2, 7, 3, 8], 10, (1, 2)),
    ([5, 3], 10, None),
    ([5], 10, None),
    ([], 10, None),
    ([5, 5], 10, (0, 1)),
    ([3, 1, 3, 4], 7, (0, 3)),
    ([0, 7, 0], 0, (0, 2)),
    ([0, 5], 5, (0, 1)),
    ([5, 1, 2], 10, None),
    ([1, 2, 3, 4, 5], 9, (3, 4)),
])
def test_find_pair(durations, slot, expected):
    assert find_pair(durations, slot) == expected


def test_many_items():
    assert find_pair(list(range(1, 60001)), 1) is None
    assert find_pair(list(range(2, 60002)) + [1], 3) == (0, 60000)
