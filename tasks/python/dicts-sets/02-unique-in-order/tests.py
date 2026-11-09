import pytest
from solution import unique_in_order


@pytest.mark.parametrize("messages, expected", [
    (["timeout", "500", "timeout", "404", "500"], ["timeout", "500", "404"]),
    (["a", "a", "a"], ["a"]),
    (["z", "b", "a"], ["z", "b", "a"]),
    (["Timeout", "timeout"], ["Timeout", "timeout"]),
    (["x", "y", "x", "z", "y"], ["x", "y", "z"]),
    ([], []),
])
def test_unique_in_order(messages, expected):
    assert unique_in_order(messages) == expected
