import json

from solution import summarize


def report(*tests):
    return json.dumps({"results": [{"name": n, "attempts": a} for n, a in tests]})


def test_example():
    text = report(("a", ["passed"]), ("b", ["failed", "passed"]), ("c", ["passed", "failed"]))
    assert summarize(text) == {"failed": ["c"], "flaky": ["b"]}


def test_all_passed():
    assert summarize(report(("a", ["passed"]), ("b", ["passed", "passed"]))) == {"failed": [], "flaky": []}


def test_failed_after_retries_is_not_flaky():
    assert summarize(report(("x", ["failed", "failed", "failed"]))) == {"failed": ["x"], "flaky": []}


def test_order_is_kept():
    text = report(("z", ["failed"]), ("a", ["failed"]), ("m", ["failed", "passed"]), ("b", ["failed", "passed"]))
    assert summarize(text) == {"failed": ["z", "a"], "flaky": ["m", "b"]}


def test_test_without_attempts_ignored():
    assert summarize(report(("a", []), ("b", ["failed"]))) == {"failed": ["b"], "flaky": []}


def test_no_results_key():
    assert summarize("{}") == {"failed": [], "flaky": []}
