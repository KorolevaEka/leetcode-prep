import pytest
from solution import integer_lines as solve

@pytest.mark.parametrize('args, expected', [((' 1\n#ignore\n-2\n\n+3',), [1, -2, 3]), (('',), []), (('  #x\n',), []), (('0\r\n10',), [0, 10])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' 1\n#ignore\n-2\n\n+3',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
