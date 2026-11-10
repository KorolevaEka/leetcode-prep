import pytest
from solution import power as solve

@pytest.mark.parametrize('args, expected', [((2, 5), 32), ((0, 0), 1), ((-2, 3), -8), ((3, 4), 81), ((0, 2), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (2, 5)
    before = deepcopy(args)
    solve(*args)
    assert args == before
