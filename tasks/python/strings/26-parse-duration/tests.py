import pytest
from solution import parse_duration


@pytest.mark.parametrize("s, expected", [
    ("1h 30m", 5400),
    ("2m5s", 125),
    ("90s", 90),
    ("1h30m15s", 5415),
    ("250ms", 0),
    ("1500ms", 1),
    ("1s500ms", 1),
    ("1s 1000ms", 2),
    ("  45s ", 45),
    ("30m1h", 5400),
    ("0s", 0),
    ("2h 5ms", 7200),
    ("1m 59s", 119),
])
def test_parse(s, expected):
    assert parse_duration(s) == expected


@pytest.mark.parametrize("s", ["", "   ", "90", "1h30", "5d", "1h 1h", "h", "1 h", "1h,30m", "5m 5m", "-5s", "1.5h", "5mss"])
def test_errors(s):
    with pytest.raises(ValueError):
        parse_duration(s)
