import pytest
from solution import same_label


@pytest.mark.parametrize("a, b, expected", [
    ("Save", "  save  ", True),
    ("Stra\u00dfe", "STRASSE", True),
    ("caf\u00e9", "cafe\u0301", True),
    ("Sa\u200bve", "Save", True),
    ("Log\u00a0in", "Log in", True),
    ("\uff2f\uff2b", "ok", True),
    ("Save", "Cancel", False),
    ("", "\u200b \u00a0\ufeff", True),
    ("a b", "ab", False),
    ("Sign   in", "sign in", True),
    ("Save\tas", "save as", True),
    ("\ufb01le", "file", True),
    ("Save", "Save!", False),
])
def test_same_label(a, b, expected):
    assert same_label(a, b) is expected
