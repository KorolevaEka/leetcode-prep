import pytest
from solution import common_tags


@pytest.mark.parametrize("suites, expected", [
    ([["api", "smoke", "fast"], ["smoke", "ui", "api"], ["api", "smoke"]], ["api", "smoke"]),
    ([["a"], ["b"]], []),
    ([["z", "z", "a"]], ["a", "z"]),
    ([], []),
    ([["x", "y"], []], []),
    ([["slow", "api", "ui"], ["ui", "slow", "api"]], ["api", "slow", "ui"]),
    ([["a", "b"], ["a", "c"], ["d"]], []),
    ([["c", "a", "b"], ["b"], ["a", "b", "b"]], ["b"]),
])
def test_common_tags(suites, expected):
    assert common_tags(suites) == expected
