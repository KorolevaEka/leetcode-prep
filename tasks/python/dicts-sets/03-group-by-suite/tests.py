import pytest
from solution import group_by_suite


@pytest.mark.parametrize("names, expected", [
    (["auth.login", "cart.add", "auth.token.expired", "smoke"],
     {"auth": ["login", "token.expired"], "cart": ["add"], "misc": ["smoke"]}),
    (["a.z", "a.b", "a.m"], {"a": ["z", "b", "m"]}),
    (["only"], {"misc": ["only"]}),
    (["x.y.z"], {"x": ["y.z"]}),
    ([], {}),
])
def test_group_by_suite(names, expected):
    result = group_by_suite(names)
    assert result == expected
    assert list(result) == list(expected)
