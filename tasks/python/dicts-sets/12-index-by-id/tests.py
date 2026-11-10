import pytest
from solution import index_by_id


@pytest.mark.parametrize("items, expected", [
    ([{"id": 1, "n": "a"}, {"id": 2, "n": "b"}, {"id": 1, "n": "c"}],
     {1: {"id": 1, "n": "c"}, 2: {"id": 2, "n": "b"}}),
    ([{"n": "no id"}], {}),
    ([], {}),
    ([{"id": "x"}], {"x": {"id": "x"}}),
    ([{"id": 5, "v": 1}, {"v": 2}, {"id": 6}], {5: {"id": 5, "v": 1}, 6: {"id": 6}}),
    ([{"id": 0, "n": "zero"}], {0: {"id": 0, "n": "zero"}}),
])
def test_index_by_id(items, expected):
    assert index_by_id(items) == expected
