import pytest
from solution import circular_gain as solve

@pytest.mark.parametrize('args, expected', [(([5, -3, 5],), 10), (([-3, -2, -4],), -2), (([],), 0), (([2],), 2), (([3, -1, 2, -1],), 4)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([5, -3, 5],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_rings_against_all_arcs():
    from itertools import product
    for n in range(1,6):
        for values in product((-2,0,3),repeat=n):
            expected=max(sum((values+values)[start:start+length]) for start in range(n) for length in range(1,n+1))
            assert solve(list(values))==expected
