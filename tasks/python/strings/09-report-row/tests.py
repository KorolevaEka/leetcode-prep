import pytest
from solution import report_row


@pytest.mark.parametrize("name, status, width, expected", [
    ("login", "PASS", 8, "login    |   PASS"),
    ("checkout", "FAIL", 3, "checkout |   FAIL"),
    ("a", "SKIPPED", 1, "a | SKIPPED"),
    ("", "OK", 2, "   |     OK"),
    ("ab", "", 4, "ab   |       "),
    ("exact", "ERROR!", 5, "exact | ERROR!"),
    ("t", "OK", 0, "t |     OK"),
])
def test_report_row(name, status, width, expected):
    assert report_row(name, status, width) == expected
