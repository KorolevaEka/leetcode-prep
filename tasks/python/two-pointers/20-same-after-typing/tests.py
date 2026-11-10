import pytest
from solution import same_after_typing


@pytest.mark.parametrize("a, b, expected", [
    ("ab#c", "ad#c", True),
    ("a#", "b#", True),
    ("#a", "a", True),
    ("a##c", "#a#c", True),
    ("abc#", "ab", True),
    ("abc", "ab", False),
    ("a#c", "b", False),
    ("", "", True),
    ("ab##", "c#d#", True),
    ("ab#c", "ac", True),
    ("x#y#z#", "", True),
    ("a#b", "b", True),
    ("ab", "ba", False),
])
def test_same_after_typing(a, b, expected):
    assert same_after_typing(a, b) == expected


def test_long_lines():
    a = "ab#" * 50000 + "z"
    b = "a#" * 50000 + "z"
    assert same_after_typing(a, "a" * 50000 + "z") is True
    assert same_after_typing(a, b) is False
