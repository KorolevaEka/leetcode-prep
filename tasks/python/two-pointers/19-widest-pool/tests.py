import random
import pytest
from solution import widest_pool


def brute(levels):
    n = len(levels)
    return max((j - i) * min(levels[i], levels[j]) for i in range(n) for j in range(i + 1, n)) if n > 1 else 0


@pytest.mark.parametrize("levels, expected", [
    ([4, 1, 7, 3, 6, 2, 5], 24),
    ([3, 3], 3),
    ([], 0),
    ([9], 0),
    ([0, 0, 0], 0),
    ([1, 8, 1], 2),
    ([5, 1, 1, 1, 5], 20),
])
def test_examples(levels, expected):
    assert widest_pool(levels) == expected


def test_random_against_brute():
    rng = random.Random(11)
    for _ in range(300):
        levels = [rng.randint(0, 15) for _ in range(rng.randint(0, 12))]
        assert widest_pool(levels) == brute(levels)


def test_large_equal():
    n = 30000
    assert widest_pool([7] * n) == 7 * (n - 1)


def test_large_staircase():
    n = 30000
    assert widest_pool(list(range(1, n + 1))) == max((n - 1 - i) * (i + 1) for i in range(n))
