import itertools
import random
import pytest
from solution import tests_that_fit as fit_tests


@pytest.mark.parametrize("durations, slots, expected", [
    ([4, 2, 7], [3, 5, 8], 3),
    ([4], [2, 5], 1),
    ([3, 1], [3], 1),
    ([2, 5], [6, 3], 2),
    ([5, 5], [5], 1),
    ([6, 7], [5], 0),
    ([], [3, 4], 0),
    ([3, 4], [], 0),
    ([1, 1, 1], [1, 1, 1], 3),
])
def test_examples(durations, slots, expected):
    assert fit_tests(durations, slots) == expected


def brute(durations, slots):
    best = 0
    for k in range(len(durations) + 1):
        for tests in itertools.combinations(durations, k):
            for perm in itertools.permutations(slots, k):
                if all(t <= s for t, s in zip(tests, perm)):
                    best = max(best, k)
    return best


def test_random_against_brute():
    rng = random.Random(3)
    for _ in range(150):
        durations = [rng.randint(1, 9) for _ in range(rng.randint(0, 5))]
        slots = [rng.randint(1, 9) for _ in range(rng.randint(0, 5))]
        assert fit_tests(durations, slots) == brute(durations, slots)
