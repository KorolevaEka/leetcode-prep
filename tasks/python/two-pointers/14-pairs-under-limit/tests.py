import random
import pytest
from solution import count_pairs_under


def brute(durations, limit):
    n = len(durations)
    return sum(1 for i in range(n) for j in range(i + 1, n) if durations[i] + durations[j] < limit)


@pytest.mark.parametrize("durations, limit, expected", [
    ([5, 1, 3, 2], 5, 2),
    ([1, 1, 1], 3, 3),
    ([4, 4], 8, 0),
    ([4, 3], 8, 1),
    ([], 10, 0),
    ([7], 100, 0),
    ([9, 8, 7], 5, 0),
    ([2, 2, 2, 2], 5, 6),
])
def test_examples(durations, limit, expected):
    assert count_pairs_under(durations, limit) == expected


def test_random_against_brute():
    rng = random.Random(7)
    for _ in range(300):
        durations = [rng.randint(0, 12) for _ in range(rng.randint(0, 12))]
        limit = rng.randint(0, 25)
        assert count_pairs_under(durations, limit) == brute(durations, limit)


def test_input_not_mutated():
    data = [5, 1, 3]
    count_pairs_under(data, 6)
    assert data == [5, 1, 3]


def test_large_equal():
    n = 30000
    assert count_pairs_under([1] * n, 3) == n * (n - 1) // 2


def test_large_buckets():
    n = 30000
    data = [i % 5 for i in range(n)]
    per = n // 5
    expected = 0
    for a in range(5):
        for b in range(a, 5):
            if a + b < 5:
                expected += per * (per - 1) // 2 if a == b else per * per
    assert count_pairs_under(data, 5) == expected
