import pytest
from solution import common_step as solve

@pytest.mark.parametrize('args, expected', [((18, 24), 6), ((7, 0), 7), ((0, 9), 9), ((13, 5), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (18, 24)
    before = deepcopy(args)
    solve(*args)
    assert args == before
