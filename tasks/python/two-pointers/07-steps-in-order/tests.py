import pytest
from solution import steps_in_order


@pytest.mark.parametrize("steps, log, expected", [
    (["login", "checkout"], ["login", "search", "checkout"], True),
    (["checkout", "login"], ["login", "search", "checkout"], False),
    ([], ["login"], True),
    ([], [], True),
    (["a"], [], False),
    (["a", "a"], ["a", "b"], False),
    (["a", "a"], ["a", "b", "a"], True),
    (["a", "b"], ["a", "x", "b"], True),
    (["a", "b", "c"], ["a", "b"], False),
    (["b"], ["a", "b", "c"], True),
])
def test_steps_in_order(steps, log, expected):
    assert steps_in_order(steps, log) is expected
