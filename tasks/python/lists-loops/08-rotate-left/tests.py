import pytest
from solution import rotate_left


@pytest.mark.parametrize("queue, k, expected", [
    (["a", "b", "c", "d"], 1, ["b", "c", "d", "a"]),
    (["a", "b", "c", "d"], 6, ["c", "d", "a", "b"]),
    (["a", "b", "c", "d"], -1, ["d", "a", "b", "c"]),
    (["a", "b", "c", "d"], 0, ["a", "b", "c", "d"]),
    (["a", "b", "c", "d"], 4, ["a", "b", "c", "d"]),
    (["a", "b", "c", "d"], -5, ["d", "a", "b", "c"]),
    (["a"], 7, ["a"]),
    ([], 3, []),
])
def test_rotate_left(queue, k, expected):
    assert rotate_left(queue, k) == expected


def test_input_not_modified():
    queue = ["a", "b", "c"]
    rotate_left(queue, 1)
    assert queue == ["a", "b", "c"]
