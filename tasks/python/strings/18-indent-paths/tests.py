import pytest
from solution import suite_paths


@pytest.mark.parametrize("text, expected", [
    ("smoke\n  login\n    ok\n  cart\nregression",
     ["smoke", "smoke/login", "smoke/login/ok", "smoke/cart", "regression"]),
    ("", []),
    ("   \n\n  ", []),
    ("only", ["only"]),
    ("a\n  b\n  c\n    d", ["a", "a/b", "a/c", "a/c/d"]),
    ("a  \n  b ", ["a", "a/b"]),
    ("a\n\n  b\n   \n  c", ["a", "a/b", "a/c"]),
    ("login ok\n  step one", ["login ok", "login ok/step one"]),
    ("a\n  b\n    c\nd\n  e", ["a", "a/b", "a/b/c", "d", "d/e"]),
])
def test_paths(text, expected):
    assert suite_paths(text) == expected


@pytest.mark.parametrize("text", ["a\n    b", "  a", "a\n b", "a\n\tb", "a\n  b\n      c"])
def test_errors(text):
    with pytest.raises(ValueError):
        suite_paths(text)
