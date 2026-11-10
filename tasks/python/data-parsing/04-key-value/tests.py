import pytest
from solution import parse_pair as solve

@pytest.mark.parametrize('args, expected', [((' host = a=b ',), ('host', 'a=b')), (('x=',), ('x', '')), (('missing',), None), ((' =1',), None)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' host = a=b ',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
