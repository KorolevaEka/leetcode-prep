import pytest
from solution import running_total


@pytest.mark.parametrize("durations, expected", [
    ([3, 1, 4], [3, 4, 8]),
    ([5], [5]),
    ([], []),
    ([0, 0, 2], [0, 0, 2]),
    ([1, 1, 1, 1], [1, 2, 3, 4]),
    ([10, -4, 2], [10, 6, 8]),
])
def test_running_total(durations, expected):
    assert running_total(durations) == expected
