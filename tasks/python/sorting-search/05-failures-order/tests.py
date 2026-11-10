import pytest
from solution import most_failing


@pytest.mark.parametrize("tests, expected", [
    ([("login", 2), ("cart", 5), ("search", 2), ("pay", 0)], ["cart", "login", "search", "pay"]),
    ([("a", 1), ("b", 1), ("c", 1)], ["a", "b", "c"]),
    ([("c", 3), ("b", 3), ("a", 3), ("d", 7)], ["d", "c", "b", "a"]),
    ([("x", 0), ("y", 4)], ["y", "x"]),
    ([("solo", 9)], ["solo"]),
    ([], []),
])
def test_most_failing(tests, expected):
    assert most_failing(tests) == expected
