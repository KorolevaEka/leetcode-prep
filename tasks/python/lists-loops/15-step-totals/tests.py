import pytest
from solution import step_totals


@pytest.mark.parametrize("runs, expected", [
    ([[1, 2, 3], [4, 5], [6]], [11, 7, 3]),
    ([[2, 2]], [2, 2]),
    ([[], [5]], [5]),
    ([], []),
    ([[1], [1, 2, 3]], [2, 2, 3]),
    ([[1, 2, 3], [1]], [2, 2, 3]),
    ([[], []], []),
    ([[1, 1], [2, 2], [3, 3]], [6, 6]),
])
def test_step_totals(runs, expected):
    assert step_totals(runs) == expected
