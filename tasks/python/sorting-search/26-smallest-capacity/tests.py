import pytest
from solution import shipping_capacity as solve

@pytest.mark.parametrize('args, expected', [(([1, 2, 3, 1, 1], 4), 3), (([], 2), 0), (([3, 2, 2, 4, 1, 4], 3), 6), (([5, 1], 9), 5), (([1, 2, 3], 1), 6)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 2, 3, 1, 1], 4)
    before = deepcopy(args)
    solve(*args)
    assert args == before
