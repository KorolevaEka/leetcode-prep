import pytest
from solution import command_words as solve

@pytest.mark.parametrize('args, expected', [(('run "a b" \'\' x\\ y',), ['run', 'a b', '', 'x y']), (('a"b"c',), ['abc']), ((" 'x\\y' ",), ['x\\y']), (('',), []), (('"bad',), '!error'), (('x\\',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('run "a b" \'\' x\\ y',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
