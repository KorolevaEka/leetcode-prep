import pytest
from solution import kth_matrix as solve

@pytest.mark.parametrize('args, expected', [(([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13), (([[-5]], 1), -5), (([[1, 1], [1, 2]], 3), 1), (([[1, 4, 7], [2, 5, 8]], 4), 5)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_matrix_rows_are_read_by_index():
    class IndexedRow(list):
        def __iter__(self):
            raise AssertionError('Разворачивать строки в плоский массив запрещено')

        def __getitem__(self, key):
            if isinstance(key, slice):
                raise AssertionError('Копировать строки запрещено')
            return super().__getitem__(key)

    matrix = [IndexedRow(range(r * 50, (r + 1) * 50)) for r in range(50)]
    assert solve(matrix, 1250) == 1249
