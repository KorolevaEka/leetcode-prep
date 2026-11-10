import pytest
from solution import nesting_depth as solve

@pytest.mark.parametrize('args, expected', [(([(5, 4), (6, 4), (6, 7), (2, 3)],), 3), (([],), 0), (([(2, 2), (2, 3), (2, 4)],), 1), (([(1, 1), (2, 2), (3, 3)],), 3), (([(1, 2), (2, 2)],), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(5, 4), (6, 4), (6, 7), (2, 3)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
