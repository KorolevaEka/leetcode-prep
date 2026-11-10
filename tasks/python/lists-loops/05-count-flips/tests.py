import pytest
from solution import count_flips


@pytest.mark.parametrize("results, expected", [
    (["passed", "failed", "failed", "passed"], 2),
    (["failed", "failed"], 0),
    (["passed"], 0),
    ([], 0),
    (["passed", "failed", "passed", "failed", "passed"], 4),
    (["failed", "passed"], 1),
    (["passed", "passed", "passed", "failed"], 1),
])
def test_count_flips(results, expected):
    assert count_flips(results) == expected
