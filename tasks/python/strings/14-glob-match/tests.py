import pytest
from solution import glob_match


@pytest.mark.parametrize("pattern, name, expected", [
    ("*.png", "a.png", True),
    ("*.png", "ui/a.png", False),
    ("**.png", "ui/a.png", True),
    ("***", "a/b/c", True),
    ("a?c", "abc", True),
    ("a?c", "a/c", False),
    ("a?c", "ac", False),
    ("[abc]x", "bx", True),
    ("[a-c]x", "dx", False),
    ("[!a-c]x", "dx", True),
    ("[!a-c]x", "bx", False),
    ("[!a]", "/", False),
    ("[a-]", "-", True),
    ("[-a]", "-", True),
    ("\\*", "*", True),
    ("\\*", "a", False),
    ("a\\?b", "a?b", True),
    ("a*", "a", True),
    ("*", "", True),
    ("", "", True),
    ("", "a", False),
    ("*a", "bab", False),
    ("*a", "bba", True),
    ("logs/*/run?.txt", "logs/ui/run1.txt", True),
    ("logs/*/run?.txt", "logs/ui/x/run1.txt", False),
    ("logs/**/run?.txt", "logs/ui/x/run1.txt", True),
    ("[a-c]*", "b/c", False),
    ("*[0-9].log", "run7.log", True),
    ("[ab]*[ab]", "abba", True),
])
def test_match(pattern, name, expected):
    assert glob_match(pattern, name) is expected


def test_many_stars_do_not_explode():
    pattern = "*a" * 14 + "*b"
    assert glob_match(pattern, "a" * 80) is False
    assert glob_match(pattern, "a" * 80 + "b") is True


@pytest.mark.parametrize("pattern", ["[abc", "[]", "[!]", "[z-a]", "abc\\", "a[", "[!"])
@pytest.mark.parametrize("name", ["", "abc"])
def test_bad_pattern(pattern, name):
    with pytest.raises(ValueError):
        glob_match(pattern, name)
