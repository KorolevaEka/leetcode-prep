import pytest
from solution import truncate


@pytest.mark.parametrize("msg, limit, expected", [
    ("Connection refused", 10, "Connect..."),
    ("Timeout", 7, "Timeout"),
    ("Timeout", 2, ".."),
    ("Timeout", 20, "Timeout"),
    ("Timeout", 0, ""),
    ("Timeout", 3, "..."),
    ("Timeout", 4, "T..."),
    ("", 0, ""),
    ("", 5, ""),
    ("ab", 1, "."),
])
def test_truncate(msg, limit, expected):
    assert truncate(msg, limit) == expected
