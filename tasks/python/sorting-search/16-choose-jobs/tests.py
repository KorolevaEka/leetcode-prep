import pytest
from solution import max_nonoverlap as solve

@pytest.mark.parametrize('args, expected', [(([(0, 10), (1, 2), (2, 3), (3, 4)],), 3), (([],), 0), (([(-5, -3), (-3, -1)],), 2), (([(0, 2), (0, 2)],), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(0, 10), (1, 2), (2, 3), (3, 4)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
