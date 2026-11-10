import pytest
from solution import closest_timeout


@pytest.mark.parametrize("allowed, wanted, expected", [
    ([30, 5, 10, 60], 12, 10),
    ([20, 10], 15, 10),
    ([10, 20], 15, 10),
    ([5, 10], 100, 10),
    ([5, 10], -3, 5),
    ([7], 1000, 7),
    ([10, 10, 20], 10, 10),
    ([1, 3], 2, 1),
    ([10, 20], 19, 20),
])
def test_closest_timeout(allowed, wanted, expected):
    assert closest_timeout(allowed, wanted) == expected
