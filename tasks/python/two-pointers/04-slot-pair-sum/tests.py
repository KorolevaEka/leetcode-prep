import pytest
from solution import fits_pair


@pytest.mark.parametrize("durations, slot, expected", [
    ([1, 3, 5, 8], 8, True),
    ([4], 8, False),
    ([4, 4], 8, True),
    ([], 5, False),
    ([1, 2, 3], 10, False),
    ([2, 6, 9], 8, True),
    ([1, 2, 3, 4], 7, True),
    ([3, 3, 3], 6, True),
    ([1, 7], 8, True),
    ([5], 10, False),
    ([0, 0], 0, True),
])
def test_fits_pair(durations, slot, expected):
    assert fits_pair(durations, slot) is expected
