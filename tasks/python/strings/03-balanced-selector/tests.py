import pytest
from solution import is_balanced


@pytest.mark.parametrize("selector, expected", [
    ("a[b(c)]{d}", True),
    ("", True),
    ("div > ul li", True),
    ("([]{})", True),
    ("a[b(c])", False),
    ("a)(", False),
    ("((", False),
    (")", False),
    ("([)]", False),
    ("([)", False),
])
def test_is_balanced(selector, expected):
    assert is_balanced(selector) is expected
