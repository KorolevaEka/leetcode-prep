import pytest
from solution import longest_common_chunk


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


def test_long_inputs():
    a = "x" * 300 + "needle" + "y" * 300
    b = "z" * 200 + "needle" + "q" * 50
    assert longest_common_chunk(a, b) == "needle"
