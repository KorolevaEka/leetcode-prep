import pytest
from solution import finish_order


@pytest.mark.parametrize("durations, quantum, expected", [
    ([5, 2, 4], 3, [1, 0, 2]),
    ([3, 3], 3, [0, 1]),
    ([1], 10, [0]),
    ([], 2, []),
    ([10, 1, 1], 4, [1, 2, 0]),
    ([4, 4, 4], 2, [0, 1, 2]),
    ([7, 3, 5], 2, [1, 2, 0]),
    ([2, 1], 1, [1, 0]),
    ([3, 2], 3, [0, 1]),
])
def test_finish_order(durations, quantum, expected):
    assert finish_order(durations, quantum) == expected


def test_many_turns():
    durations = [1000] * 50
    assert finish_order(durations, 1) == list(range(50))
