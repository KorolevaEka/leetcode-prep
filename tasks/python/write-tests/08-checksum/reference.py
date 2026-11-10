import pytest
from solution import check_digit as solve

@pytest.mark.parametrize('args, expected', [(('123',), 4), (('',), 0), (('55',), 0), (('9',), 1), (('000',), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('123',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
