import pytest
from solution import missing_fields


@pytest.mark.parametrize("response, required, expected", [
    ({"id": 7, "name": None, "tags": []}, ["id", "name", "email", "tags"], ["name", "email"]),
    ({"count": 0, "ok": False}, ["ok", "count"], []),
    ({}, ["id"], ["id"]),
    ({"a": 1}, [], []),
    ({"title": ""}, ["title"], []),
    ({"z": 1}, ["z", "b", "a"], ["b", "a"]),
    ({"extra": 1, "id": None}, ["id"], ["id"]),
])
def test_missing_fields(response, required, expected):
    assert missing_fields(response, required) == expected
