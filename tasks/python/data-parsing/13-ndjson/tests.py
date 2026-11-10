import pytest
from solution import parse_ndjson as solve

@pytest.mark.parametrize('args, expected', [(('1\n\nBAD\n{"x":2}',), ([1, {'x': 2}], [3])), (('',), ([], [])), (('null\nfalse\n0',), ([None, False, 0], [])), (('bad\n[]\n?',), ([[]], [1, 3]))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('1\n\nBAD\n{"x":2}',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
