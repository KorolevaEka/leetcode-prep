import pytest
from solution import parse_indented as solve

@pytest.mark.parametrize('args, expected', [(('a:\n  x: 1\n  b:\n    y: z\nc: q',), {'a': {'x': '1', 'b': {'y': 'z'}}, 'c': 'q'}), (('',), {}), (('a: 1\na: 2',), '!error'), (('a: 1\n  b: 2',), '!error'), (('a:\n    b: 2',), '!error'), (('a:\n  x: 1\nb:\n  x: 2',), {'a': {'x': '1'}, 'b': {'x': '2'}})])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('a:\n  x: 1\n  b:\n    y: z\nc: q',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
