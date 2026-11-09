import pytest
from solution import count_statuses


@pytest.mark.parametrize("statuses, expected", [
    (["passed", "failed", "passed"], {"passed": 2, "failed": 1}),
    (["skipped"], {"skipped": 1}),
    (["failed", "failed", "failed"], {"failed": 3}),
    (["a", "b", "c", "b", "a", "a"], {"a": 3, "b": 2, "c": 1}),
    ([], {}),
])
def test_count_statuses(statuses, expected):
    assert count_statuses(statuses) == expected
