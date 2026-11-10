import pytest
from solution import rename_cost


@pytest.mark.parametrize("old, new, expected", [
    ("Login_Test", "login_test", 0),
    ("ab", "ba", 1),
    ("ca", "abc", 3),
    ("smoke", "some", 2),
    ("", "", 0),
    ("abc", "", 3),
    ("", "abc", 3),
    ("same", "SAME", 0),
    ("test_a", "test_b", 1),
    ("abcd", "acbd", 1),
    ("kitten", "sitting", 3),
    ("checkout", "chekcout", 1),
    ("flaky", "fake", 2),
    ("abab", "baba", 2),
    ("ba", "ab", 1),
])
def test_cost(old, new, expected):
    assert rename_cost(old, new) == expected


def test_long_names():
    assert rename_cost("ab" * 150, "ba" * 150) == 2
    assert rename_cost("x" * 300, "y" * 300) == 300
