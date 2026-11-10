import pytest
from solution import json_field as solve

@pytest.mark.parametrize('args, expected', [(('{"x":0}', 'x'), 0), (('{"x":false}', 'x'), False), (('{}', 'x'), None), (('{"x":[1,2]}', 'x'), [1, 2])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('{"x":0}', 'x')
    before = deepcopy(args)
    solve(*args)
    assert args == before
