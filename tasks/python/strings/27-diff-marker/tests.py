import pytest
from solution import diff_marker


@pytest.mark.parametrize("expected, actual, result", [
    ("hello world", "hello wide world", "hello w[-+ide w]orld"),
    ("cat", "cut", "c[-a+u]t"),
    ("aa", "aaa", "aa[-+a]"),
    ("same", "same", "same"),
    ("", "", ""),
    ("", "x", "[-+x]"),
    ("x", "", "[-x+]"),
    ("abcabc", "abc", "abc[-abc+]"),
    ("xyz", "abc", "[-xyz+abc]"),
    ("status=ok", "status=fail", "status=[-ok+fail]"),
    ("abXab", "abYab", "ab[-X+Y]ab"),
    ("aaa", "aa", "aa[-a+]"),
])
def test_diff_marker(expected, actual, result):
    assert diff_marker(expected, actual) == result
