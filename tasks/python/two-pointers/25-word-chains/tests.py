import pytest
from solution import chain_starts as solve

@pytest.mark.parametrize('args, expected', [(('barfoofoobarthefoobarman', ['bar', 'foo', 'the']), [6, 9, 12]), (('', []), []), (('aaaaaa', ['aa', 'aa']), [0, 1, 2]), (('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good']), [8]), (('xbarfoo', ['bar', 'foo']), [1])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('barfoofoobarthefoobarman', ['bar', 'foo', 'the'])
    before = deepcopy(args)
    solve(*args)
    assert args == before
