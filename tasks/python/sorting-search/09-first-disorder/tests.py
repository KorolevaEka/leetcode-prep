import pytest
from solution import first_disorder


@pytest.mark.parametrize("timestamps, expected", [
    ([1, 2, 2, 5, 4, 9, 3], 4),
    ([1, 2, 2, 3], -1),
    ([5], -1),
    ([], -1),
    ([2, 1], 1),
    ([3, 3, 3], -1),
    ([1, 5, 6, 7, 0], 4),
    ([9, 1, 2], 1),
])
def test_first_disorder(timestamps, expected):
    assert first_disorder(timestamps) == expected
