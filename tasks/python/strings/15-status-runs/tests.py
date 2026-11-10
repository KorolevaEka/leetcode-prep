import pytest
from solution import compress_statuses


@pytest.mark.parametrize("s, expected", [
    ("PPPFFP", "P3F2P1"),
    ("Pp", "P1p1"),
    ("", ""),
    ("P", "P1"),
    ("ab", "a1b1"),
    ("aaaaaaaaaaaa", "a12"),
    ("PPFFPP", "P2F2P2"),
    ("FFFF", "F4"),
    ("PFPFP", "P1F1P1F1P1"),
])
def test_compress_statuses(s, expected):
    assert compress_statuses(s) == expected
