import pytest
from solution import json_types as solve

@pytest.mark.parametrize('args, expected', [(('[null,true,0,"",[],{}]',), ['null', 'bool', 'number', 'string', 'array', 'object']), (('[]',), []), (('[false,1.5]',), ['bool', 'number']), (('[[1],[null]]',), ['array', 'array'])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('[null,true,0,"",[],{}]',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
