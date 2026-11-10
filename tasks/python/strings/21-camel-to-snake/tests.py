import pytest
from solution import camel_to_snake


@pytest.mark.parametrize("name, expected", [
    ("getUserName", "get_user_name"),
    ("HTTPServerError", "http_server_error"),
    ("user2Id", "user2_id"),
    ("already_snake", "already_snake"),
    ("Name", "name"),
    ("", ""),
    ("A", "a"),
    ("parseHTML5Doc", "parse_html5_doc"),
    ("XMLHttpRequest", "xml_http_request"),
    ("userID", "user_id"),
    ("plain", "plain"),
    ("get_userName", "get_user_name"),
])
def test_camel_to_snake(name, expected):
    assert camel_to_snake(name) == expected
