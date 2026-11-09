import pytest
from solution import merge_windows


@pytest.mark.parametrize("windows, expected", [
    ([[60, 90], [10, 30], [25, 40]], [[10, 40], [60, 90]]),
    ([[0, 10], [10, 20]], [[0, 20]]),
    ([[0, 100], [10, 20]], [[0, 100]]),
    ([[0, 5], [10, 15]], [[0, 5], [10, 15]]),
    ([[5, 6]], [[5, 6]]),
    ([], []),
])
def test_merge_windows(windows, expected):
    assert merge_windows(windows) == expected


def test_input_not_modified():
    windows = [[20, 30], [0, 25]]
    merge_windows(windows)
    assert windows == [[20, 30], [0, 25]]
