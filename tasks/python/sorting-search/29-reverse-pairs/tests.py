import pytest
from solution import drop_pairs as solve

@pytest.mark.parametrize('args, expected', [(([1, 3, 2, 3, 1],), 2), (([2, 4, 3, 5, 1],), 3), (([],), 0), (([-5, -5],), 1), (([2, 1],), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3, 2, 3, 1],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_inputs_against_pair_definition():
    from itertools import product
    for n in range(6):
        for values in product((-2,0,2),repeat=n):
            expected=sum(values[i]>2*values[j] for i in range(n) for j in range(i+1,n))
            assert solve(list(values))==expected
