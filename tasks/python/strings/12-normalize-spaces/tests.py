import pytest
from solution import clean_message


@pytest.mark.parametrize("text, expected", [
    ("a\n\t b  ", "a b"),
    ("  Error:\r\n  boom", "Error: boom"),
    (" \t\n ", ""),
    ("", ""),
    ("single", "single"),
    ("a  b   c", "a b c"),
    ("line1\nline2", "line1 line2"),
    ("\n\nTrace\n\tat x\n", "Trace at x"),
    ("a\tb", "a b"),
])
def test_clean_message(text, expected):
    assert clean_message(text) == expected
