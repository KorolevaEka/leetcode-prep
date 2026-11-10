import pytest
from solution import flaky_tests


@pytest.mark.parametrize("runs, expected", [
    ([("login", True), ("cart", False), ("login", False), ("pay", True), ("cart", False), ("pay", True)], ["login"]),
    ([("a", False), ("a", False)], []),
    ([("a", True)], []),
    ([], []),
    ([("z", True), ("b", True), ("b", False), ("z", False)], ["z", "b"]),
    ([("x", True), ("x", True), ("x", False)], ["x"]),
    ([("x", False), ("x", True), ("x", True)], ["x"]),
    ([("m", True), ("m", False), ("m", True), ("m", False)], ["m"]),
    ([("a", True), ("b", False), ("c", True), ("a", False), ("b", True)], ["a", "b"]),
])
def test_flaky_tests(runs, expected):
    assert flaky_tests(runs) == expected
