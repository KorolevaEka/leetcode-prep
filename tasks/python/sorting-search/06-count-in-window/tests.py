import pytest
from solution import count_between

class Probe:
    def __init__(self, data):
        self.data = data
        self.reads = 0

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        if isinstance(i, slice):
            raise TypeError("срезы запрещены")
        self.reads += 1
        return self.data[i]


@pytest.mark.parametrize("timestamps, start, end, expected", [
    ([1, 3, 3, 5, 8], 3, 5, 3),
    ([1, 3, 3, 5, 8], 4, 4, 0),
    ([1, 3, 3, 5, 8], 9, 2, 0),
    ([1, 3, 3, 5, 8], 0, 100, 5),
    ([1, 3, 3, 5, 8], 8, 8, 1),
    ([1, 3, 3, 5, 8], 1, 1, 1),
    ([1, 3, 3, 5, 8], 6, 7, 0),
    ([4], 4, 4, 1),
    ([], 1, 5, 0),
])
def test_count_between(timestamps, start, end, expected):
    assert count_between(timestamps, start, end) == expected


def test_large_input_few_reads():
    probe = Probe(list(range(0, 2_000_000, 2)))
    assert count_between(probe, 1000, 1999) == 500
    assert count_between(probe, -5, 3) == 2
    assert count_between(probe, 1_999_990, 5_000_000) == 5
    assert probe.reads <= 200
