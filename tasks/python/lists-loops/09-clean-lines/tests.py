import pytest
from solution import clean_lines


@pytest.mark.parametrize("lines, expected", [
    (["  user=anna ", "", "# note", "   ", "mode=fast"], ["user=anna", "mode=fast"]),
    (["  # note", "a # b"], ["a # b"]),
    ([], []),
    (["", "  ", "\t"], []),
    (["\tx\t"], ["x"]),
    (["b", "a", "b"], ["b", "a", "b"]),
    (["#", "# a", "#a"], []),
])
def test_clean_lines(lines, expected):
    assert clean_lines(lines) == expected
