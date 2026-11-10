import pytest
from solution import batches

def test_complete_and_tail():
    assert list(batches(iter([1, 2, 3, 4, 5]), 2)) == [[1, 2], [3, 4], [5]]

def test_empty_and_exact_multiple():
    assert list(batches(iter([]), 2)) == []
    assert list(batches(iter([1, 2]), 2)) == [[1, 2]]

def test_consumption_is_lazy():
    seen = []

    def source():
        for i in range(5):
            seen.append(i)
            yield i
    result = batches(source(), 2)
    assert seen == []
    assert next(result) == [0, 1]
    assert seen == [0, 1]
    assert next(result) == [2, 3]
    assert seen == [0, 1, 2, 3]

def test_invalid_size():
    with pytest.raises(ValueError):
        next(batches(iter([1]), 0))
