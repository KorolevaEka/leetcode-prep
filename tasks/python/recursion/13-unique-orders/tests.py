import pytest
from solution import unique_orders as solve

@pytest.mark.parametrize('args, expected', [(([1, 1, 2],), [[1, 1, 2], [1, 2, 1], [2, 1, 1]]), (([],), [[]]), (([2],), [[2]]), (([2, 1],), [[1, 2], [2, 1]])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 1, 2],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
