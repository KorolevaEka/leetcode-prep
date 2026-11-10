import pytest
from solution import matrix_cost as solve

@pytest.mark.parametrize('args, expected', [(([10, 30, 5, 60],), 4500), (([5, 10],), 0), (([],), 0), (([2, 3, 4],), 24), (([40, 20, 30, 10, 30],), 26000)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([10, 30, 5, 60],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
