import pytest
from solution import order_results


@pytest.mark.parametrize("results, expected", [
    ([("b", "passed"), ("a", "failed"), ("c", "flaky"), ("a", "passed")],
     [("a", "failed"), ("c", "flaky"), ("a", "passed"), ("b", "passed")]),
    ([("z", "skipped"), ("y", "flaky"), ("x", "failed"), ("w", "failed")],
     [("w", "failed"), ("x", "failed"), ("y", "flaky"), ("z", "skipped")]),
    ([("a", "passed"), ("b", "skipped")], [("b", "skipped"), ("a", "passed")]),
    ([("only", "passed")], [("only", "passed")]),
    ([], []),
])
def test_order_results(results, expected):
    assert order_results(results) == expected


def test_input_not_modified():
    results = [("b", "passed"), ("a", "failed")]
    order_results(results)
    assert results == [("b", "passed"), ("a", "failed")]
