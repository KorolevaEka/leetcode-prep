import pytest
from solution import cap_repeats


@pytest.mark.parametrize("ids, k, expected", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 1, 2, 2, 3]),
    ([1, 1, 1, 2, 2, 3], 1, [1, 2, 3]),
    ([1, 1, 1, 2, 2, 3], 0, []),
    ([], 3, []),
    ([5, 5, 5, 5], 3, [5, 5, 5]),
    ([1, 1, 1, 1, 2], 5, [1, 1, 1, 1, 2]),
    ([1, 1, 1, 1, 2, 2, 2, 3], 2, [1, 1, 2, 2, 3]),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([4, 4, 4, 4, 4, 4], 4, [4, 4, 4, 4]),
])
def test_cap_repeats(ids, k, expected):
    assert cap_repeats(ids, k) == expected


def test_input_not_mutated():
    data = [1, 1, 1, 2]
    cap_repeats(data, 1)
    assert data == [1, 1, 1, 2]
