from solution import count_exact_distinct


def test_examples():
    assert count_exact_distinct([1, 2, 1, 2, 3], 2) == 7
    assert count_exact_distinct([1, 1, 1], 1) == 6
    assert count_exact_distinct([1, 2], 3) == 0


def test_zero_and_empty():
    assert count_exact_distinct([1, 2, 3], 0) == 0
    assert count_exact_distinct([], 1) == 0
    assert count_exact_distinct([], 0) == 0


def test_k_equals_all_distinct():
    assert count_exact_distinct([1, 2, 3], 3) == 1
    assert count_exact_distinct([1, 2, 3], 1) == 3


def test_repeats_inside():
    assert count_exact_distinct([1, 2, 1, 3, 4], 3) == 3
    assert count_exact_distinct([4, 4, 5, 5, 4], 2) == 8


def test_matches_brute_force():
    import random
    rng = random.Random(5)
    for _ in range(300):
        codes = [rng.randint(1, 4) for _ in range(rng.randint(0, 12))]
        k = rng.randint(0, 5)
        expected = sum(1 for i in range(len(codes)) for j in range(i + 1, len(codes) + 1) if len(set(codes[i:j])) == k)
        assert count_exact_distinct(codes, k) == expected


def test_large_few_codes():
    codes = [i % 3 for i in range(100_000)]
    n = len(codes)
    assert count_exact_distinct(codes, 3) == (n - 2) * (n - 1) // 2
    assert count_exact_distinct(codes, 1) == n


def test_large_many_codes():
    codes = list(range(100_000))
    assert count_exact_distinct(codes, 5) == 100_000 - 4
