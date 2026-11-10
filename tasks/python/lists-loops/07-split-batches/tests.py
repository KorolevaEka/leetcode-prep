import pytest
from solution import split_batches


@pytest.mark.parametrize("tests, size, expected", [
    (["a", "b", "c", "d", "e"], 2, [["a", "b"], ["c", "d"], ["e"]]),
    (["a", "b"], 5, [["a", "b"]]),
    ([], 3, []),
    (["a", "b", "c", "d"], 2, [["a", "b"], ["c", "d"]]),
    (["a", "b", "c"], 1, [["a"], ["b"], ["c"]]),
    (["a"], 1, [["a"]]),
])
def test_split_batches(tests, size, expected):
    assert split_batches(tests, size) == expected
