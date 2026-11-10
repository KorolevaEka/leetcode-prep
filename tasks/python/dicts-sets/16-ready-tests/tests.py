import pytest
from solution import ready_tests

DEPS = {"cart": ["login"], "pay": ["login", "cart"], "login": [], "logout": ["login"]}


@pytest.mark.parametrize("deps, done, expected", [
    (DEPS, ["login"], ["cart", "logout"]),
    (DEPS, [], ["login"]),
    ({"a": ["setup"]}, [], []),
    ({"a": ["setup"]}, ["setup"], ["a"]),
    (DEPS, ["login", "cart", "logout"], ["pay"]),
    (DEPS, ["login", "cart", "pay", "logout"], []),
    ({}, ["x"], []),
    ({"z": [], "b": [], "a": []}, ["b"], ["z", "a"]),
    ({"t": ["p", "q"]}, ["p"], []),
    ({"t": ["p", "q"]}, ["q", "p"], ["t"]),
])
def test_ready_tests(deps, done, expected):
    assert ready_tests(deps, done) == expected
