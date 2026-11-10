import pytest
from solution import count_shuffled_windows


@pytest.mark.parametrize("log, pattern, expected", [
    (list("abcbaca"), list("abc"), 3),
    (list("aabab"), list("aab"), 2),
    (list("xabc"), list("abc"), 1),
    (list("abc"), list("abcd"), 0),
    (list("abc"), [], 0),
    ([], list("a"), 0),
    (list("aaaa"), list("aa"), 3),
    (list("abab"), list("ab"), 3),
    (list("abc"), list("abc"), 1),
    (["login", "open", "login", "close", "open"], ["open", "login"], 2),
])
def test_examples(log, pattern, expected):
    assert count_shuffled_windows(log, pattern) == expected


def test_large_log():
    log = ["a", "b"] * 150000
    pattern = ["a"] * 7500 + ["b"] * 7500
    assert count_shuffled_windows(log, pattern) == 300000 - 15000 + 1
