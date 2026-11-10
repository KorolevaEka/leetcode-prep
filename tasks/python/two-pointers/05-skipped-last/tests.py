import pytest
from solution import skipped_last


@pytest.mark.parametrize("results, expected", [
    (["passed", "skipped", "failed", "skipped", "passed"],
     ["passed", "failed", "passed", "skipped", "skipped"]),
    (["skipped"], ["skipped"]),
    ([], []),
    (["passed", "failed"], ["passed", "failed"]),
    (["skipped", "skipped", "failed"], ["failed", "skipped", "skipped"]),
    (["failed", "passed", "skipped"], ["failed", "passed", "skipped"]),
    (["skipped", "passed", "failed"], ["passed", "failed", "skipped"]),
])
def test_skipped_last(results, expected):
    assert skipped_last(results) == expected


def test_input_is_not_changed():
    results = ["skipped", "passed"]
    skipped_last(results)
    assert results == ["skipped", "passed"]
