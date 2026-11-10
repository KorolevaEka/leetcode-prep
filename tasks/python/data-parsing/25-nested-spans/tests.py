import pytest
from solution import exclusive_times as solve

@pytest.mark.parametrize('args, expected', [(([('a', 'start', 0), ('b', 'start', 2), ('b', 'end', 5), ('a', 'end', 7)],), {'a': 4, 'b': 3}), (([],), {}), (([('a', 'start', 0), ('a', 'start', 1), ('a', 'end', 3), ('a', 'end', 4)],), {'a': 4}), (([('a', 'start', 0), ('b', 'end', 1)],), '!error'), (([('a', 'start', 2), ('a', 'end', 1)],), '!error'), (([('a', 'start', 0)],), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([('a', 'start', 0), ('b', 'start', 2), ('b', 'end', 5), ('a', 'end', 7)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
