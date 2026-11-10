from solution import count_quads


def test_examples():
    assert count_quads([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert count_quads([0], [0], [0], [0]) == 1
    assert count_quads([], [1], [1], [1]) == 0


def test_no_solution():
    assert count_quads([1], [1], [1], [1]) == 0


def test_equal_values_are_different_index_tuples():
    assert count_quads([1, 1], [-1, -1], [0, 0], [0, 0]) == 16


def test_sum_reachable_many_ways():
    assert count_quads([1, 2], [3, 2], [-4, -4], [-1, -1]) == 4


def test_zero_sum_not_only_by_zeros():
    assert count_quads([5], [-5], [7], [-7]) == 1


def test_different_list_lengths():
    assert count_quads([1, 2, 3], [-1], [-2, 0], [2, 1, 0]) == 4


def test_matches_brute_force():
    import random
    from itertools import product
    rng = random.Random(9)
    for _ in range(100):
        lists = [[rng.randint(-3, 3) for _ in range(rng.randint(0, 5))] for _ in range(4)]
        expected = sum(1 for t in product(*lists) if sum(t) == 0)
        assert count_quads(*lists) == expected


def test_large():
    n = 300
    a = [i % 7 - 3 for i in range(n)]
    b = [i % 5 - 2 for i in range(n)]
    c = [-(i % 7) + 3 for i in range(n)]
    d = [-(i % 5) + 2 for i in range(n)]
    from collections import Counter
    ab = Counter(x + y for x in a for y in b)
    expected = sum(ab[-(x + y)] for x in c for y in d)
    assert count_quads(a, b, c, d) == expected
    assert count_quads([0] * n, [0] * n, [0] * n, [0] * n) == n ** 4
