import pytest
from solution import parse_row


@pytest.mark.parametrize("line, expected", [
    ("1,Ann,ann@test.io", ["1", "Ann", "ann@test.io"]),
    ('2,"Smith, Bob",ok', ["2", "Smith, Bob", "ok"]),
    ('3,"say ""hi""",x', ["3", 'say "hi"', "x"]),
    ("a,,", ["a", "", ""]),
    ("a,b,", ["a", "b", ""]),
    ('"only, one"', ["only, one"]),
    ('""""', ['"']),
    ("", [""]),
])
def test_parse_row(line, expected):
    assert parse_row(line) == expected
