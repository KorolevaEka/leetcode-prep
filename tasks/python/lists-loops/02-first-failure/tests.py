import pytest
from solution import first_failure


@pytest.mark.parametrize("statuses, expected", [
    (["passed", "skipped", "failed", "failed"], 2),
    (["failed"], 0),
    (["failed", "passed"], 0),
    (["passed", "passed", "failed"], 2),
    (["passed", "passed"], -1),
    ([], -1),
])
def test_first_failure(statuses, expected):
    assert first_failure(statuses) == expected
