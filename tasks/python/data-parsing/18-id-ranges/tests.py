import pytest
from solution import parse_id_ranges as solve

@pytest.mark.parametrize('args, expected', [((' 1-3,2,5 ',), [1, 2, 3, 5]), (('',), []), (('0-0',), [0]), (('3-1',), '!error'), (('1,,2',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' 1-3,2,5 ',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
