import pytest
from solution import slugify


@pytest.mark.parametrize("title, expected", [
    ("Login: SSO, retry #2", "login-sso-retry-2"),
    ("  Checkout   Flow  ", "checkout-flow"),
    ("Already-slug", "already-slug"),
    ("A", "a"),
    ("!!!", ""),
    ("", ""),
])
def test_slugify(title, expected):
    assert slugify(title) == expected
