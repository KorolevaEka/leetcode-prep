import random
from solution import longest_run


def test_examples():
    assert longest_run([7, 3, 4, 100, 5, 4, 6]) == [3, 4, 5, 6, 7]
    assert longest_run([1, 2, 10, 11]) == [1, 2]
    assert longest_run([]) == []


def test_single_and_all_equal():
    assert longest_run([5]) == [5]
    assert longest_run([4, 4, 4]) == [4]


def test_duplicates_do_not_extend():
    assert longest_run([1, 1, 2, 2, 3, 3, 9, 9, 9, 9]) == [1, 2, 3]
    assert longest_run([1, 1, 1, 1, 5, 6]) == [5, 6]


def test_tie_smaller_start():
    assert longest_run([20, 21, 22, 1, 2, 3]) == [1, 2, 3]
    assert longest_run([1, 2, 3, 20, 21, 22]) == [1, 2, 3]


def test_negative_and_unordered():
    assert longest_run([0, -1, -2, 5, 1, 2]) == [-2, -1, 0, 1, 2]


def test_gap_of_one_breaks_run():
    assert longest_run([1, 2, 4, 5, 6]) == [4, 5, 6]


def test_matches_brute_force():
    rng = random.Random(3)
    for _ in range(200):
        ids = [rng.randint(-8, 8) for _ in range(rng.randint(0, 15))]
        s = set(ids)
        best = []
        for x in sorted(s):
            run = [x]
            while run[-1] + 1 in s:
                run.append(run[-1] + 1)
            if len(run) > len(best):
                best = run
        assert longest_run(ids) == best


def test_large_single_run():
    ids = list(range(200_000))
    random.Random(1).shuffle(ids)
    assert longest_run(ids) == list(range(200_000))


def test_large_with_noise():
    ids = list(range(0, 150_000)) + list(range(1_000_000, 1_000_000 + 50_000)) + [5] * 1000
    random.Random(2).shuffle(ids)
    assert longest_run(ids) == list(range(150_000))
