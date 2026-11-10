import pytest
from solution import interleave


@pytest.mark.parametrize("a, b, expected", [
    (["a1", "a2"], ["b1", "b2"], ["a1", "b1", "a2", "b2"]),
    (["a1", "a2", "a3"], ["b1"], ["a1", "b1", "a2", "a3"]),
    (["a1"], ["b1", "b2", "b3"], ["a1", "b1", "b2", "b3"]),
    ([], ["b1", "b2"], ["b1", "b2"]),
    (["a1"], [], ["a1"]),
    ([], [], []),
])
def test_interleave(a, b, expected):
    assert interleave(a, b) == expected
