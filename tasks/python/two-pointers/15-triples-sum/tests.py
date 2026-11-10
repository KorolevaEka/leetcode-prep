import pytest
from solution import triples_with_sum


@pytest.mark.parametrize("values, target, expected", [
    ([-1, 0, 1, 2, -1, -4], 0, [(-1, -1, 2), (-1, 0, 1)]),
    ([0, 0, 0, 0], 0, [(0, 0, 0)]),
    ([-2, 0, 0, 2, 2], 0, [(-2, 0, 2)]),
    ([1, 2, 3], 5, []),
    ([1, 2, 3], 6, [(1, 2, 3)]),
    ([1, 1], 2, []),
    ([], 0, []),
    ([5, 5, 5], 15, [(5, 5, 5)]),
    ([3, 1, 2, 4, 5], 9, [(1, 3, 5), (2, 3, 4)]),
])
def test_examples(values, target, expected):
    assert triples_with_sum(values, target) == expected


def test_large_none():
    assert triples_with_sum([2 * i for i in range(1000)], 1) == []


def test_large_many():
    n = 1000
    expected = [(2 * i, 2 * j, 2 * (1500 - i - j))
                for i in range(n) for j in range(i + 1, n) if j < 1500 - i - j <= n - 1]
    assert triples_with_sum([2 * i for i in range(n)], 3000) == expected
