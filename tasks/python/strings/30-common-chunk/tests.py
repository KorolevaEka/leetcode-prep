import sys

_saved = sys.modules.get("difflib")
sys.modules["difflib"] = None
import pytest
from solution import longest_common_chunk
if _saved is None:
    del sys.modules["difflib"]
else:
    sys.modules["difflib"] = _saved


@pytest.mark.parametrize("a, b, expected", [
    ("timeout at login", "timeout at checkout", "timeout at "),
    ("abXcd", "cdYab", "ab"),
    ("abc", "xyz", ""),
    ("", "abc", ""),
    ("abc", "", ""),
    ("ABC", "abc", ""),
    ("axbxc", "abc", "a"),
    ("xabcy", "zabcw", "abc"),
    ("aaaa", "aa", "aa"),
    ("abcabc", "abc", "abc"),
    ("ababc", "abcab", "abc"),
    ("same", "same", "same"),
])
def test_chunk(a, b, expected):
    assert longest_common_chunk(a, b) == expected


def test_long_periodic_inputs():
    a = "ab" * 700 + "x"
    b = "ab" * 700 + "y"
    assert longest_common_chunk(a, b) == "ab" * 700


def test_long_shifted_inputs():
    a = "ab" * 700
    b = "ba" * 700
    assert longest_common_chunk(a, b) == ("ab" * 700)[:-1]


def test_long_without_common():
    assert longest_common_chunk("x" * 1400 + "needle", "y" * 1400 + "needle") == "needle"
