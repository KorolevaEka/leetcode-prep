import pytest
from solution import inversion_count as solve

@pytest.mark.parametrize('args, expected', [(([3, 1, 2],), 2), (([],), 0), (([2, 2],), 0), (([4, 3, 2, 1],), 6), (([-1, -2, 0],), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([3, 1, 2],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_large_descending_order():
    n=30000
    assert solve(list(range(n,0,-1)))==n*(n-1)//2
