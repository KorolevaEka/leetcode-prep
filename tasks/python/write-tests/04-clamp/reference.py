import pytest
from solution import clamp as solve

@pytest.mark.parametrize('args, expected', [((5, 0, 10), 5), ((-3, -2, 4), -2), ((12, 0, 10), 10), ((2, 2, 2), 2), ((0, 5, 1), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (5, 0, 10)
    before = deepcopy(args)
    solve(*args)
    assert args == before
