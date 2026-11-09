import pytest
from solution import flatten


@pytest.mark.parametrize("items, expected", [
    (["smoke", ["auth", ["login", "logout"]], "cart"], ["smoke", "auth", "login", "logout", "cart"]),
    ([[], ["a"], [[]]], ["a"]),
    ([[["x", ["y", ["z"]]]]], ["x", "y", "z"]),
    (["a", "", "b"], ["a", "", "b"]),
    (["a", "b"], ["a", "b"]),
    ([], []),
])
def test_flatten(items, expected):
    assert flatten(items) == expected


def test_input_not_modified():
    items = ["a", ["b", ["c"]]]
    flatten(items)
    assert items == ["a", ["b", ["c"]]]
