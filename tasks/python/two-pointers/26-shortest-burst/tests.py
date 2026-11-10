import pytest
from solution import shortest_burst as solve

@pytest.mark.parametrize('args, expected', [(([2, -1, 2], 3), 3), (([], 1), -1), (([1, 2], 4), -1), (([84, -37, 32, 40, 95], 167), 3), (([2, -5, 7], 7), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([2, -1, 2], 3)
    before = deepcopy(args)
    solve(*args)
    assert args == before
