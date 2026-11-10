import pytest
from solution import is_anagram


@pytest.mark.parametrize("a, b, expected", [
    ("Dormitory", "dirty room", True),
    ("aab", "abb", False),
    ("abc", "abcd", False),
    ("", "", True),
    ("   ", "", True),
    ("Listen", "Silent", True),
    ("aabb", "ab", False),
    ("abc1", "1cba", True),
    ("a", "b", False),
])
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) is expected
