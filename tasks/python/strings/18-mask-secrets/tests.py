import pytest
from solution import mask_secrets


@pytest.mark.parametrize("line, keys, expected", [
    ("GET /x?user=bob&Password=hunter2&next=1", ["password"], "GET /x?user=bob&Password=***&next=1"),
    ("mypassword=1", ["password"], "mypassword=1"),
    ("a=1 token=xyz b=2", ["token"], "a=1 token=*** b=2"),
    ("token=abc", [], "token=abc"),
    ("a?TOKEN=abc def", ["token"], "a?TOKEN=*** def"),
    ("mypassword=1&password=2", ["password"], "mypassword=1&password=***"),
    ("token=&x=1", ["token"], "token=***&x=1"),
    ("k=1&secret=2&pass=3", ["secret", "pass"], "k=1&secret=***&pass=***"),
    ("a.b=1&axb=2", ["a.b"], "a.b=***&axb=2"),
    ("password=a=b&x=1", ["password"], "password=***&x=1"),
    ("no secrets here", ["password"], "no secrets here"),
    ("passwordx=1", ["password"], "passwordx=1"),
])
def test_mask_secrets(line, keys, expected):
    assert mask_secrets(line, keys) == expected
