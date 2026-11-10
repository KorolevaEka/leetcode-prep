import pytest
from solution import ticket_cost as solve

@pytest.mark.parametrize('args, expected', [(([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11), (([], [2, 7, 15]), 0), (([1, 1, 1], [2, 7, 15]), 2), (([7, 1, 8], [3, 4, 100]), 7), (([1, 7], [5, 6, 20]), 6)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 4, 6, 7, 8, 20], [2, 7, 15])
    before = deepcopy(args)
    solve(*args)
    assert args == before
