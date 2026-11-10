import pytest
from solution import is_mirror_code


@pytest.mark.parametrize("code, expected", [
    ("Ab-ba", True),
    ("ab a", False),
    ("A-b-c", False),
    ("", True),
    ("x", True),
    ("--", True),
    ("ab-a", True),
    ("RaceCar", True),
    ("a_b-ba", False),
    ("abca", False),
])
def test_is_mirror_code(code, expected):
    assert is_mirror_code(code) is expected
