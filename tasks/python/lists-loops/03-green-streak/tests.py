import pytest
from solution import longest_green_streak


@pytest.mark.parametrize("builds, expected", [
    (["green", "green", "red", "green"], 2),
    (["red", "red"], 0),
    (["green", "green", "green"], 3),
    (["green", "red", "green", "green", "green", "red", "green"], 3),
    (["red", "green", "green"], 2),
    (["green"], 1),
    ([], 0),
])
def test_longest_green_streak(builds, expected):
    assert longest_green_streak(builds) == expected
