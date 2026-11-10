import pytest
from solution import retry_delays


@pytest.mark.parametrize("retries, base, cap, expected", [
    (4, 1, 100, [1, 2, 4, 8]),
    (5, 3, 20, [3, 6, 12, 20, 20]),
    (0, 1, 10, []),
    (1, 5, 5, [5]),
    (3, 2, 2, [2, 2, 2]),
    (6, 1, 16, [1, 2, 4, 8, 16, 16]),
])
def test_retry_delays(retries, base, cap, expected):
    assert retry_delays(retries, base, cap) == expected
