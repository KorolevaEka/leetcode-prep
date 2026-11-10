import pytest
from solution import deep_merge


@pytest.mark.parametrize("base, override, expected", [
    ({"db": {"host": "qa", "port": 5432}, "tags": ["a"], "debug": False},
     {"db": {"port": 6000}, "tags": ["b"], "retries": 3},
     {"db": {"host": "qa", "port": 6000}, "tags": ["b"], "debug": False, "retries": 3}),
    ({}, {}, {}),
    ({"a": 1}, {}, {"a": 1}),
    ({}, {"a": {"b": 1}}, {"a": {"b": 1}}),
    ({"a": {"b": 1}}, {"a": 5}, {"a": 5}),
    ({"a": 5}, {"a": {"b": 1}}, {"a": {"b": 1}}),
    ({"a": {"b": {"c": 1, "d": 2}}}, {"a": {"b": {"c": 9}}}, {"a": {"b": {"c": 9, "d": 2}}}),
    ({"a": {"b": 1}}, {"a": None}, {"a": None}),
    ({"a": [1, 2]}, {"a": [3]}, {"a": [3]}),
    ({"a": {"x": 1}}, {"a": {}}, {"a": {"x": 1}}),
])
def test_deep_merge(base, override, expected):
    assert deep_merge(base, override) == expected


def test_inputs_not_changed():
    base = {"db": {"host": "qa", "port": 1}, "tags": ["a"]}
    override = {"db": {"port": 2}, "other": {"k": [1]}}
    deep_merge(base, override)
    assert base == {"db": {"host": "qa", "port": 1}, "tags": ["a"]}
    assert override == {"db": {"port": 2}, "other": {"k": [1]}}


def test_result_is_independent():
    base = {"db": {"host": "qa"}, "tags": ["a"], "solo": {"x": 1}}
    override = {"db": {"port": 1}, "extra": {"k": [1]}}
    result = deep_merge(base, override)
    result["db"]["host"] = "changed"
    result["tags"].append("b")
    result["solo"]["x"] = 99
    result["extra"]["k"].append(2)
    assert base == {"db": {"host": "qa"}, "tags": ["a"], "solo": {"x": 1}}
    assert override == {"db": {"port": 1}, "extra": {"k": [1]}}
