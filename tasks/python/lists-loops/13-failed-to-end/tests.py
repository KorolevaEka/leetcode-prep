import pytest
from solution import move_failed_last


def make(spec):
    return [{"name": name, "status": status} for name, status in spec]


def names(results):
    return [r["name"] for r in results]


@pytest.mark.parametrize("spec, expected", [
    ([("a", "failed"), ("b", "passed"), ("c", "failed"), ("d", "skipped")], ["b", "d", "a", "c"]),
    ([("a", "passed"), ("b", "skipped")], ["a", "b"]),
    ([("a", "failed"), ("b", "failed")], ["a", "b"]),
    ([("a", "failed"), ("b", "passed"), ("c", "passed")], ["b", "c", "a"]),
    ([("z", "passed"), ("y", "failed"), ("x", "passed"), ("w", "failed")], ["z", "x", "y", "w"]),
    ([], []),
])
def test_order(spec, expected):
    results = make(spec)
    assert move_failed_last(results) is None
    assert names(results) == expected


def test_in_place_same_objects():
    results = make([("a", "failed"), ("b", "passed")])
    same_list = results
    originals = list(results)
    move_failed_last(results)
    assert results is same_list
    assert results[0] is originals[1] and results[1] is originals[0]
