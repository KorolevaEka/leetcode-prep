import random
from collections import Counter

import pytest
from solution import shortest_prefixes


@pytest.mark.parametrize("names, expected", [
    (["login_ok", "login_fail", "logout", "cart"], ["login_o", "login_f", "logo", "c"]),
    (["ab", "abc"], ["ab", "abc"]),
    (["x"], ["x"]),
    ([], []),
    (["a", "ab", "ac"], ["a", "ab", "ac"]),
    (["A", "a"], ["A", "a"]),
    (["b", "a"], ["b", "a"]),
    (["test_1", "test_2", "test_10"], ["test_1", "test_2", "test_10"]),
    (["smoke_ui", "smoke_api", "smoke"], ["smoke_u", "smoke_a", "smoke"]),
])
def test_examples(names, expected):
    assert shortest_prefixes(names) == expected


def test_many_names():
    names = [f"login_{i:05d}" for i in range(20000)]
    random.Random(7).shuffle(names)
    result = shortest_prefixes(names)
    prefixes = Counter(name[:k] for name in names for k in range(1, len(name) + 1))
    for name, short in zip(names, result):
        assert name.startswith(short)
        assert prefixes[short] == 1
        assert len(short) == 1 or prefixes[short[:-1]] > 1
