import pytest
from solution import sum_digits


@pytest.mark.parametrize("n, expected", [
    (1234, 10),
    (10, 1),
    (7, 7),
    (0, 0),
    (9, 9),
    (100, 1),
    (90909, 27),
])
def test_sum_digits(n, expected):
    assert sum_digits(n) == expected
