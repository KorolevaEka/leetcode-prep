import pytest
from solution import json_pointer as solve

@pytest.mark.parametrize('args, expected', [(({'a/b': {'~x': [7]}}, '/a~1b/~0x/0'), 7), (({'': 2}, '/'), 2), (([1], ''), [1]), (([1], '/01'), '!error'), (({'~1': 'x'}, '/~01'), 'x'), (({}, '/x'), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'a/b': {'~x': [7]}}, '/a~1b/~0x/0')
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_leading_zero_with_valid_numeric_index():
    with pytest.raises(ValueError):
        solve([10, 20], '/01')
