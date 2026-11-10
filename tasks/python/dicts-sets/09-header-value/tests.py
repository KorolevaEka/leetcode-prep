import pytest
from solution import header_value


@pytest.mark.parametrize("headers, name, expected", [
    ({"Content-Type": "text/html"}, "content-type", "text/html"),
    ({"x-id": "1", "X-ID": "2"}, "X-Id", "1"),
    ({"Accept": "*/*"}, "Content-Type", None),
    ({}, "Accept", None),
    ({"ETAG": "abc"}, "etag", "abc"),
    ({"a": "", "b": "1"}, "A", ""),
    ({"X-Token": "t"}, "X-Token", "t"),
])
def test_header_value(headers, name, expected):
    assert header_value(headers, name) == expected
