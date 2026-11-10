import random
from functools import lru_cache

import pytest
from solution import balanced_wrap


@pytest.mark.parametrize("text, width, expected", [
    ("aaa bb cc ddddd", 6, ["aaa", "bb cc", "ddddd"]),
    ("one two", 100, ["one two"]),
    ("", 5, []),
    ("  \n ", 5, []),
    ("one", 10, ["one"]),
    ("abcdefgh x", 3, ["abcdefgh", "x"]),
    ("test run test test run test", 8, ["test run", "test", "test run", "test"]),
    ("a   b\tc", 5, ["a b c"]),
    ("ab cd ef", 2, ["ab", "cd", "ef"]),
    ("a bbbbbbbbbb c d", 4, ["a", "bbbbbbbbbb", "c d"]),
])
def test_examples(text, width, expected):
    assert balanced_wrap(text, width) == expected


def line_cost(line, width):
    return 0 if len(line) > width else (width - len(line)) ** 2


def best_cost(words, width):
    @lru_cache(None)
    def go(i):
        if i == len(words):
            return 0
        options = []
        for j in range(i + 1, len(words) + 1):
            line = " ".join(words[i:j])
            if len(line) > width and j - i > 1:
                break
            options.append((0 if j == len(words) else line_cost(line, width)) + go(j))
        return min(options)
    return go(0)


def test_large_text_is_optimal():
    rnd = random.Random(11)
    words = tuple("w" * rnd.randint(1, 9) for _ in range(300))
    lines = balanced_wrap(" ".join(words), 30)
    assert " ".join(lines).split() == list(words)
    assert all(len(l) <= 30 or " " not in l for l in lines)
    total = sum(line_cost(l, 30) for l in lines[:-1])
    assert total == best_cost(words, 30)
