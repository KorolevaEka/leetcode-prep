import itertools
import pytest
from solution import best_stretch


@pytest.mark.parametrize("deltas, expected", [
    ([2, -1, 3, -5, 4], (0, 2, 4)),
    ([-3, -1, -2], (1, 1, -1)),
    ([1, -1, 1], (0, 0, 1)),
    ([5], (0, 0, 5)),
    ([-4], (0, 0, -4)),
    ([0, 0], (0, 0, 0)),
    ([-1, 2, -2, 2], (1, 1, 2)),
    ([-2, 1, 1, -5, 4], (4, 4, 4)),
    ([3, -3, 3, -3, 3], (0, 0, 3)),
    ([1, 2, -10, 5, 5], (3, 4, 10)),
])
def test_best_stretch(deltas, expected):
    assert best_stretch(deltas) == expected


def test_matches_brute_force_on_small_inputs():
    for deltas in itertools.product([-2, 0, 1, 3], repeat=5):
        deltas = list(deltas)
        brute = max(((s, e, sum(deltas[s:e + 1])) for s in range(5) for e in range(s, 5)),
                    key=lambda t: (t[2], -t[0], -t[1]))
        assert best_stretch(deltas) == brute


def test_long_input():
    deltas = [1, -1] * 20000 + [5]
    assert best_stretch(deltas) == (0, 40000, 5)
