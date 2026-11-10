import pytest
from solution import expand_pattern


@pytest.mark.parametrize("p, expected", [
    ("user{1..3}@x.io", ["user1@x.io", "user2@x.io", "user3@x.io"]),
    ("n{08..10}", ["n08", "n09", "n10"]),
    ("{1..2}-{1..2}", ["1-1", "1-2", "2-1", "2-2"]),
    ("plain", ["plain"]),
    ("", [""]),
    ("{5..5}", ["5"]),
    ("{x} {1..}", ["{x} {1..}"]),
    ("{001..003}", ["001", "002", "003"]),
    ("{9..11}", ["9", "10", "11"]),
    ("u{1..2}-{1..3}", ["u1-1", "u1-2", "u1-3", "u2-1", "u2-2", "u2-3"]),
    ("a{0..2}", ["a0", "a1", "a2"]),
    ("{1..2}{01..02}", ["101", "102", "201", "202"]),
])
def test_expand(p, expected):
    assert expand_pattern(p) == expected


@pytest.mark.parametrize("p", ["{3..1}", "u{1..2}-{5..4}", "{2..1}-{1..2}"])
def test_reversed_range(p):
    with pytest.raises(ValueError):
        expand_pattern(p)
