import pytest
from solution import top_error


@pytest.mark.parametrize("errors, expected", [
    (["timeout", "404", "timeout", "500"], "timeout"),
    (["b", "a", "a", "b"], "b"),
    ([], None),
    (["only"], "only"),
    (["z", "y", "x"], "z"),
    (["a", "b", "b", "c", "c", "a", "c"], "c"),
    (["q", "w", "w", "q", "e", "e"], "q"),
    (["x", "z", "z", "x"], "x"),
])
def test_top_error(errors, expected):
    assert top_error(errors) == expected
