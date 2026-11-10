import pytest
from solution import longest_clean_run


@pytest.mark.parametrize("events, expected", [
    (list("abcabcbb"), 3),
    (list("bbbb"), 1),
    ([], 0),
    (["a"], 1),
    (list("abba"), 2),
    (list("abcbdea"), 5),
    (list("pwwkew"), 3),
    (list("tmmzuxt"), 5),
    (list("abcdef"), 6),
])
def test_longest_clean_run(events, expected):
    assert longest_clean_run(events) == expected


def test_words():
    log = ["login", "open", "click", "open", "wait", "logout", "login"]
    assert longest_clean_run(log) == 5
