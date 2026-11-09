import pytest
from solution import shortest_chunk


@pytest.mark.parametrize("log, required, expected", [
    (["login", "click", "error", "click", "login", "error"], {"login", "error"}, 2),
    (["a", "b", "a", "c"], {"a", "b", "c"}, 3),
    (["a", "a"], {"a", "b"}, -1),
    (["a", "x", "x", "b", "a"], {"a", "b"}, 2),
    (["a", "a", "a", "b"], {"a", "b"}, 2),
    (["b", "a", "b", "a", "c"], {"a", "b", "c"}, 3),
    (["x"], {"x"}, 1),
    (["x", "y"], set(), 0),
    ([], {"a"}, -1),
])
def test_shortest_chunk(log, required, expected):
    assert shortest_chunk(log, required) == expected
