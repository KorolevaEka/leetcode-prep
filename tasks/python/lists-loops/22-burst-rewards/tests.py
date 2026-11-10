import pytest
from solution import max_cleanup as solve

@pytest.mark.parametrize('args, expected', [(([3, 1, 5, 8],), 167), (([],), 0), (([4],), 4), (([2, 3],), 9), (([1, 1, 1],), 3)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([3, 1, 5, 8],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
