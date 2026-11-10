import pytest
from solution import digit_product as solve

@pytest.mark.parametrize('args, expected', [((234,), 24), ((0,), 0), ((105,), 0), ((7,), 7), ((111,), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (234,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
