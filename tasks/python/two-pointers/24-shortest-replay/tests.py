import pytest
from solution import shortest_replay as solve

@pytest.mark.parametrize('args, expected', [((['a', 'b', 'c', 'd', 'e', 'b', 'd', 'd', 'e'], ['b', 'd', 'e']), ['b', 'c', 'd', 'e']), (([], ['a']), []), ((['a'], []), []), ((['a', 'a', 'a', 'b'], ['a', 'b']), ['a', 'b']), ((['a', 'b', 'x', 'b', 'a'], ['a', 'a']), ['a', 'b', 'x', 'b', 'a']), ((['a', 'b', 'b', 'a'], ['b', 'a']), ['b', 'a'])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['a', 'b', 'c', 'd', 'e', 'b', 'd', 'd', 'e'], ['b', 'd', 'e'])
    before = deepcopy(args)
    solve(*args)
    assert args == before
