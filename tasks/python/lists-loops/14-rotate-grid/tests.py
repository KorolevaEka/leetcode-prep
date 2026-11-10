import pytest
from solution import rotate_grid


@pytest.mark.parametrize("grid, expected", [
    ([["a", "b", "c"], ["d", "e", "f"]], [["d", "a"], ["e", "b"], ["f", "c"]]),
    ([["a", "b"], ["c", "d"]], [["c", "a"], ["d", "b"]]),
    ([["x"]], [["x"]]),
    ([], []),
    ([["a", "b", "c"]], [["a"], ["b"], ["c"]]),
    ([["a"], ["b"], ["c"]], [["c", "b", "a"]]),
    ([["1", "2"], ["3", "4"], ["5", "6"], ["7", "8"]], [["7", "5", "3", "1"], ["8", "6", "4", "2"]]),
])
def test_rotate_grid(grid, expected):
    assert rotate_grid(grid) == expected


def test_input_not_modified():
    grid = [["a", "b", "c"], ["d", "e", "f"]]
    rotate_grid(grid)
    assert grid == [["a", "b", "c"], ["d", "e", "f"]]
