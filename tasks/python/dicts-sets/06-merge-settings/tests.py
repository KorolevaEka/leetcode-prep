import pytest
from solution import merge_settings


@pytest.mark.parametrize("defaults, overrides, expected", [
    ({"retries": 3, "env": "qa"}, {"retries": 0, "debug": True}, {"retries": 0, "env": "qa", "debug": True}),
    ({"proxy": "p1", "env": "qa"}, {"proxy": None}, {"env": "qa"}),
    ({}, {}, {}),
    ({"a": 1}, {}, {"a": 1}),
    ({}, {"a": 1}, {"a": 1}),
    ({"a": 1}, {"b": None}, {"a": 1}),
    ({"flag": True, "name": "x"}, {"flag": False, "name": ""}, {"flag": False, "name": ""}),
])
def test_merge_settings(defaults, overrides, expected):
    assert merge_settings(defaults, overrides) == expected


def test_inputs_not_changed():
    defaults, overrides = {"a": 1, "b": 2}, {"a": None, "c": 3}
    merge_settings(defaults, overrides)
    assert defaults == {"a": 1, "b": 2}
    assert overrides == {"a": None, "c": 3}
