import pytest
from solution import common_ids


@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 2, 3, 5], [2, 2, 4, 5], [2, 5]),
    ([], [1], []),
    ([1], [], []),
    ([1, 2], [3, 4], []),
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
    ([1, 1, 1], [1], [1]),
    ([4, 6, 9], [1, 4, 5, 6], [4, 6]),
    ([1, 5], [1, 5, 5, 5], [1, 5]),
    ([1, 2], [0, 1, 2], [1, 2]),
])
def test_common_ids(a, b, expected):
    assert common_ids(a, b) == expected
