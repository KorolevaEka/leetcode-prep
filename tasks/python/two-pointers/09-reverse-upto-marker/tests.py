import pytest
from solution import reverse_upto


@pytest.mark.parametrize("items, stop, expected", [
    ([1, 2, 3, 4], 3, [3, 2, 1, 4]),
    ([2, 1, 3, 1, 4], 1, [1, 2, 3, 1, 4]),
    ([1, 2, 3], 9, [1, 2, 3]),
    ([], 1, []),
    ([5, 6], 5, [5, 6]),
    ([1, 2, 1, 3], 1, [1, 2, 1, 3]),
    (["a", "b", "c"], "c", ["c", "b", "a"]),
    ([7], 7, [7]),
])
def test_reverse_upto(items, stop, expected):
    assert reverse_upto(items, stop) == expected


def test_input_is_not_changed():
    items = [1, 2, 3]
    reverse_upto(items, 3)
    assert items == [1, 2, 3]
