import pytest
from solution import rebuild_tree as solve

@pytest.mark.parametrize('args, expected', [((['a', 'b', 'd', 'c'], ['b', 'd', 'a', 'c']), ('a', ('b', None, ('d', None, None)), ('c', None, None))), (([], []), None), ((['x'], ['x']), ('x', None, None)), ((['a', 'b', 'c'], ['c', 'b', 'a']), ('a', ('b', ('c', None, None), None), None))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['a', 'b', 'd', 'c'], ['b', 'd', 'a', 'c'])
    before = deepcopy(args)
    solve(*args)
    assert args == before
