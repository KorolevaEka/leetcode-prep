import pytest
from solution import common_range as solve

@pytest.mark.parametrize('args, expected', [(([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],), (20, 24)), (([],), None), (([[1], []],), None), (([[1, 4], [2, 5]],), (1, 2)), (([[3, 3], [3]],), (3, 3))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
