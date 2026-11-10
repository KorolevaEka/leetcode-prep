import pytest
from solution import diff_configs


@pytest.mark.parametrize("old, new, expected", [
    ({"a": 1, "b": 2, "c": 3}, {"b": 20, "c": 3, "d": 4},
     {"added": ["d"], "removed": ["a"], "changed": ["b"]}),
    ({}, {}, {"added": [], "removed": [], "changed": []}),
    ({"x": 1}, {"x": 1}, {"added": [], "removed": [], "changed": []}),
    ({}, {"b": 1, "a": 2}, {"added": ["a", "b"], "removed": [], "changed": []}),
    ({"z": 1, "y": 2}, {}, {"added": [], "removed": ["y", "z"], "changed": []}),
    ({"b": 1, "a": 1}, {"a": 2, "b": 2}, {"added": [], "removed": [], "changed": ["a", "b"]}),
    ({"k": None}, {"k": 0}, {"added": [], "removed": [], "changed": ["k"]}),
])
def test_diff_configs(old, new, expected):
    assert diff_configs(old, new) == expected
