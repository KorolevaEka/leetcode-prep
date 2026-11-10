import pytest
from solution import is_valid_version


@pytest.mark.parametrize("s, expected", [
    ("v2.0.10", True),
    ("1.2.3-rc.1", True),
    ("1.02.3", False),
    ("1.2.3-", False),
    ("1.2.3", True),
    ("0.0.0", True),
    ("10.20.30-beta", True),
    ("1.2", False),
    ("1.2.3.4", False),
    ("v", False),
    ("V1.2.3", False),
    ("1.2.3-beta_1", False),
    ("1.2.3-a-b", False),
    ("", False),
    ("1.2.x", False),
    ("1.2.3 ", False),
    ("01.2.3", False),
])
def test_is_valid_version(s, expected):
    assert is_valid_version(s) is expected
