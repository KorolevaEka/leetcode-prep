import pytest
from solution import launch_orders as solve

@pytest.mark.parametrize('args, expected', [((4,), 24), ((0,), 1), ((1,), 1), ((5,), 120)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (4,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
