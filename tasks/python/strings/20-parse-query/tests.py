import pytest
from solution import parse_query


@pytest.mark.parametrize("qs, expected", [
    ("?a=1&b=2&b=3", {"a": "1", "b": ["2", "3"]}),
    ("flag&x=a=b", {"flag": "", "x": "a=b"}),
    ("?", {}),
    ("", {}),
    ("a=1&&b=2&", {"a": "1", "b": "2"}),
    ("=v&a=1", {"a": "1"}),
    ("tag=x&tag=y&tag=z", {"tag": ["x", "y", "z"]}),
    ("a=1&a=", {"a": ["1", ""]}),
    ("q=%20+x", {"q": "%20+x"}),
    ("??a=1", {"?a": "1"}),
    ("a=1&b=2&a=3", {"a": ["1", "3"], "b": "2"}),
    ("k=", {"k": ""}),
])
def test_parse_query(qs, expected):
    assert parse_query(qs) == expected
