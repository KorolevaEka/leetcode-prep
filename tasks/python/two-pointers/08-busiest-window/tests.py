from itertools import accumulate

import pytest
from solution import busiest_window


@pytest.mark.parametrize("rps, k, expected", [
    ([5, 1, 3, 7, 2], 2, 10),
    ([4], 1, 4),
    ([1, 2], 3, 0),
    ([], 1, 0),
    ([2, 2, 2, 9], 4, 15),
    ([1, 1, 1, 9, 9], 2, 18),
    ([9, 1, 1, 1], 2, 10),
    ([0, 0, 0], 2, 0),
])
def test_busiest_window(rps, k, expected):
    assert busiest_window(rps, k) == expected


def test_long_run():
    n, k = 200_000, 20_000
    rps = [(i * 37) % 101 for i in range(n)]
    prefix = [0] + list(accumulate(rps))
    expected = max(prefix[i + k] - prefix[i] for i in range(n - k + 1))
    assert busiest_window(rps, k) == expected
