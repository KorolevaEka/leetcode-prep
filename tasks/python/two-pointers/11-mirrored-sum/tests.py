import pytest
from solution import mirrored_sum


@pytest.mark.parametrize("values, total, expected", [
    ([3, 4, 5, 6, 7], 10, True),
    ([3, 4, 5, 6, 8], 10, False),
    ([1, 9], 10, True),
    ([5], 10, True),
    ([4], 10, False),
    ([], 10, True),
    ([3, 1, 2, 7], 10, False),
    ([4, 2, 8, 5], 10, False),
    ([2, 8, 2, 8], 10, True),
    ([0, 0, 0], 0, True),
])
def test_mirrored_sum(values, total, expected):
    assert mirrored_sum(values, total) is expected
