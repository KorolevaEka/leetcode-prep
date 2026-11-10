import pytest
from solution import missing_ranges


@pytest.mark.parametrize("found, lo, hi, expected", [
    ([3, 4, 7], 1, 9, ["1-2", "5-6", "8-9"]),
    ([1, 2, 3], 1, 3, []),
    ([2, 4], 1, 5, ["1", "3", "5"]),
    ([], 5, 8, ["5-8"]),
    ([], 5, 5, ["5"]),
    ([5], 5, 5, []),
    ([1], 1, 4, ["2-4"]),
    ([4], 1, 4, ["1-3"]),
    ([10, 11, 12], 10, 20, ["13-20"]),
    ([0, 100], 0, 100, ["1-99"]),
])
def test_missing_ranges(found, lo, hi, expected):
    assert missing_ranges(found, lo, hi) == expected
