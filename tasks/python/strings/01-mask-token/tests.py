import pytest
from solution import mask_token


@pytest.mark.parametrize("token, expected", [
    ("abcd1234efgh", "********efgh"),
    ("12345", "*2345"),
    ("abcd", "abcd"),
    ("xyz", "xyz"),
    ("", ""),
])
def test_mask_token(token, expected):
    assert mask_token(token) == expected
