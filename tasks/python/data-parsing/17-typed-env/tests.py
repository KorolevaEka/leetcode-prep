import pytest
from solution import typed_env as solve

@pytest.mark.parametrize('args, expected', [(({'a': ' -2 ', 'b': ' FALSE ', 'c': ' x ', 'other': '7'}, {'a': 'int', 'b': 'bool', 'c': 'str'}), {'a': -2, 'b': False, 'c': ' x '}), (({}, {'a': 'int'}), {}), (({'a': 'yes'}, {'a': 'bool'}), '!error'), (({'a': 'oops'}, {'a': 'int'}), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'a': ' -2 ', 'b': ' FALSE ', 'c': ' x ', 'other': '7'}, {'a': 'int', 'b': 'bool', 'c': 'str'})
    before = deepcopy(args)
    solve(*args)
    assert args == before
