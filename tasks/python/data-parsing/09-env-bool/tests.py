import pytest
from solution import parse_flag as solve

@pytest.mark.parametrize('args, expected', [((' YES ',), True), (('0',), False), (('',), None), (('maybe',), None), (('False',), False)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' YES ',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
