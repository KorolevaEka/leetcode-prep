import pytest
from solution import wrap_text


@pytest.mark.parametrize("text, width, expected", [
    ("run all smoke tests now", 10, ["run all", "smoke", "tests now"]),
    ("a extraordinarily b", 5, ["a", "extraordinarily", "b"]),
    ("", 10, []),
    ("   \n ", 10, []),
    ("aaa bbb ccc", 7, ["aaa bbb", "ccc"]),
    ("a   b", 10, ["a b"]),
    ("one two", 100, ["one two"]),
    ("abcdef", 3, ["abcdef"]),
    ("ab cd ef", 2, ["ab", "cd", "ef"]),
    ("x\ny\tz", 3, ["x y", "z"]),
])
def test_wrap_text(text, width, expected):
    assert wrap_text(text, width) == expected
