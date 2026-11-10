import pytest
from solution import trapped_water as solve

@pytest.mark.parametrize('args, expected', [(([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6), (([],), 0), (([3, 0, 3],), 3), (([3, 0, 1],), 1), (([1, 2, 3],), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
