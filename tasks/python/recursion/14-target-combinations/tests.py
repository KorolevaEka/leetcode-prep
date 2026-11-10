import pytest
from solution import budget_combinations as solve

@pytest.mark.parametrize('args, expected', [(([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]), (([], 0), [[]]), (([2, 2, 2], 4), [[2, 2]]), (([3], 2), [])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([10, 1, 2, 7, 6, 1, 5], 8)
    before = deepcopy(args)
    solve(*args)
    assert args == before
