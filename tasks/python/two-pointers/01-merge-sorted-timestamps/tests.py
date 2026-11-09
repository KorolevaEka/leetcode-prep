import pytest
from solution import merge_logs


@pytest.mark.parametrize("a, b, expected", [
    ([1, 4, 9], [2, 3, 10, 11], [1, 2, 3, 4, 9, 10, 11]),
    ([5, 5], [5], [5, 5, 5]),
    ([], [7], [7]),
    ([7], [], [7]),
    ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5]),
    ([4, 5], [1, 2, 3], [1, 2, 3, 4, 5]),
    ([], [], []),
])
def test_merge_logs(a, b, expected):
    assert merge_logs(a, b) == expected
