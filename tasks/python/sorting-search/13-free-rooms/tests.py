import pytest
from solution import room_count as solve

@pytest.mark.parametrize('args, expected', [(([(0, 5), (2, 7), (5, 8)],), 2), (([],), 0), (([(1, 2), (2, 3)],), 1), (([(0, 4), (0, 4), (0, 4)],), 3), (([(-2, 0), (0, 2)],), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(0, 5), (2, 7), (5, 8)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
