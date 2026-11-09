import pytest
from solution import average_duration


@pytest.mark.parametrize("durations, expected", [
    ([1.5, 2.5, 4], 2.67),
    ([3], 3.0),
    ([1, 2], 1.5),
    ([0, 0, 0], 0.0),
    ([], 0.0),
])
def test_average_duration(durations, expected):
    assert average_duration(durations) == expected
