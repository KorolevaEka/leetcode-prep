from solution import count_spans


def test_examples():
    assert count_spans([1, 2, 3], 3) == 2
    assert count_spans([1, -1, 0], 0) == 3
    assert count_spans([], 0) == 0


def test_whole_list_and_prefix():
    assert count_spans([5], 5) == 1
    assert count_spans([2, 3, 5], 10) == 1
    assert count_spans([2, 3, 5], 5) == 2


def test_nothing_matches():
    assert count_spans([1, 2, 3], 100) == 0
    assert count_spans([1, 1, 1], 0) == 0


def test_same_sum_many_times():
    assert count_spans([1, 1, 1], 2) == 2
    assert count_spans([0, 0, 0], 0) == 6
    assert count_spans([1, -1, 1, -1], 0) == 4


def test_negative_numbers():
    assert count_spans([-1, -1, 1], 0) == 1
    assert count_spans([3, -3, 3, -3, 3], 3) == 6


def test_matches_brute_force():
    import random
    rng = random.Random(7)
    for _ in range(200):
        vals = [rng.randint(-3, 3) for _ in range(rng.randint(0, 12))]
        k = rng.randint(-4, 4)
        expected = sum(1 for i in range(len(vals)) for j in range(i + 1, len(vals) + 1) if sum(vals[i:j]) == k)
        assert count_spans(vals, k) == expected


def test_large_all_zeros():
    n = 200_000
    assert count_spans([0] * n, 0) == n * (n + 1) // 2


def test_large_alternating():
    m = 100_000
    assert count_spans([1, -1] * m, 0) == (m + 1) * m // 2 + m * (m - 1) // 2
