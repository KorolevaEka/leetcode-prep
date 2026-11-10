import pytest
from solution import left_join


@pytest.mark.parametrize("left, right, key, expected", [
    ([{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}],
     [{"id": 1, "sum": 5}, {"id": 1, "sum": 7}], "id",
     [{"id": 1, "name": "Ann", "sum": 5}, {"id": 1, "name": "Ann", "sum": 7}, {"id": 2, "name": "Bob"}]),
    ([], [{"id": 1}], "id", []),
    ([{"id": 1}], [], "id", [{"id": 1}]),
    ([{"id": 1, "v": "L"}], [{"id": 1, "v": "R"}], "id", [{"id": 1, "v": "R"}]),
    ([{"name": "x"}], [{"name": "y"}], "id", [{"name": "x"}]),
    ([{"id": None, "a": 1}, {"b": 2}], [{"id": None, "c": 3}, {"d": 4}], "id",
     [{"id": None, "a": 1, "c": 3}, {"b": 2}]),
    ([{"id": 2}, {"id": 1}], [{"id": 1, "z": 1}, {"id": 2, "z": 2}], "id",
     [{"id": 2, "z": 2}, {"id": 1, "z": 1}]),
    ([{"id": 1}, {"id": 1}], [{"id": 1, "o": "a"}], "id", [{"id": 1, "o": "a"}, {"id": 1, "o": "a"}]),
])
def test_left_join(left, right, key, expected):
    assert left_join(left, right, key) == expected


def test_inputs_not_changed():
    left = [{"id": 1, "a": 1}]
    right = [{"id": 1, "b": 2}]
    result = left_join(left, right, "id")
    result[0]["a"] = 99
    assert left == [{"id": 1, "a": 1}]
    assert right == [{"id": 1, "b": 2}]
    unmatched = left_join(left, [], "id")
    unmatched[0]["a"] = 5
    assert left == [{"id": 1, "a": 1}]
