import pytest
from solution import percentile


@pytest.mark.parametrize("samples, p, expected", [
    ([15, 20, 35, 40, 50], 30, 20),
    ([15, 20, 35, 40, 50], 40, 20),
    ([15, 20, 35, 40, 50], 50, 35),
    ([50, 15, 40, 20, 35], 100, 50),
    ([50, 15, 40, 20, 35], 1, 15),
    ([7], 95, 7),
    (list(range(1, 21)), 95, 19),
    (list(range(20, 0, -1)), 90, 18),
])
def test_percentile(samples, p, expected):
    assert percentile(samples, p) == expected


def test_input_not_modified():
    samples = [3, 1, 2]
    percentile(samples, 50)
    assert samples == [3, 1, 2]
