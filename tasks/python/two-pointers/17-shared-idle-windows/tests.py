import pytest
from solution import shared_windows


@pytest.mark.parametrize("a, b, min_len, expected", [
    ([(0, 5), (8, 12)], [(3, 9), (10, 20)], 2, [(3, 5), (10, 12)]),
    ([(0, 10)], [(1, 3), (5, 8)], 2, [(1, 3), (5, 8)]),
    ([(0, 5)], [(5, 9)], 1, []),
    ([(0, 3), (3, 5)], [(1, 4)], 1, [(1, 3), (3, 4)]),
    ([], [(1, 4)], 1, []),
    ([(1, 4)], [], 1, []),
    ([(0, 10)], [(2, 4)], 5, []),
    ([(0, 4), (6, 9)], [(0, 4), (6, 9)], 3, [(0, 4), (6, 9)]),
    ([(2, 7)], [(0, 3), (4, 5), (6, 20)], 1, [(2, 3), (4, 5), (6, 7)]),
])
def test_shared_windows(a, b, min_len, expected):
    assert shared_windows(a, b, min_len) == expected
