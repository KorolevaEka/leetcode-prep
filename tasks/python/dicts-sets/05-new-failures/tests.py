import pytest
from solution import new_failures


@pytest.mark.parametrize("previous, current, expected", [
    (["login", "cart"], ["cart", "pay", "search", "pay"], ["pay", "search"]),
    (["a"], ["a", "a"], []),
    ([], ["b", "a"], ["b", "a"]),
    (["x"], [], []),
    ([], [], []),
    (["m", "n"], ["z", "y", "z", "m", "y"], ["z", "y"]),
    (["Login"], ["login"], ["login"]),
])
def test_new_failures(previous, current, expected):
    assert new_failures(previous, current) == expected


def test_inputs_not_changed():
    previous, current = ["a"], ["b", "b"]
    new_failures(previous, current)
    assert previous == ["a"] and current == ["b", "b"]
