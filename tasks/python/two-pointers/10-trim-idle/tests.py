import pytest
from solution import trim_idle


@pytest.mark.parametrize("samples, expected", [
    ([0, 0, 5, 0, 3, 0], [5, 0, 3]),
    ([0, 0], []),
    ([], []),
    ([7], [7]),
    ([0, 4], [4]),
    ([4, 0], [4]),
    ([1, 0, 0, 2], [1, 0, 0, 2]),
    ([0], []),
    ([0, 0, 0, 1, 0, 0], [1]),
])
def test_trim_idle(samples, expected):
    assert trim_idle(samples) == expected
