from solution import leaf_paths


def test_example():
    data = {"id": 7, "user": {"name": "Ann", "tags": ["a", "b"]}, "items": [{"id": 1}], "note": None}
    assert leaf_paths(data) == ["id", "user.name", "user.tags[0]", "user.tags[1]", "items[0].id", "note"]


def test_empty_containers_are_leaves():
    assert leaf_paths({"a": {}, "b": [], "c": 0}) == ["a", "b", "c"]


def test_falsy_values_are_leaves():
    assert leaf_paths({"a": 0, "b": "", "c": False, "d": None}) == ["a", "b", "c", "d"]


def test_nested_lists():
    assert leaf_paths({"m": [[1, 2], [3]]}) == ["m[0][0]", "m[0][1]", "m[1][0]"]


def test_deep_dicts():
    assert leaf_paths({"a": {"b": {"c": 1}}}) == ["a.b.c"]


def test_empty():
    assert leaf_paths({}) == []
