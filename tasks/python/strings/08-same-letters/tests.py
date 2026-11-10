import pytest
from solution import is_anagram


@pytest.mark.parametrize("a, b, expected", [
    ("run_42", "24_NUR", True),
    ("ui smoke", "MOKESIU", True),
    ("ttest", "tesst", False),
    ("pass", "fail", False),
    ("abc", "abcd", False),
    ("", "", True),
    ("   ", "", True),
    ("aabb", "ab", False),
    ("e2e", "ee2", True),
    ("a", "b", False),
])
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) is expected
