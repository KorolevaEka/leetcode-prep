import pytest
from solution import skyline as solve

@pytest.mark.parametrize('args, expected', [(([(1, 4, 3), (2, 6, 5), (6, 7, 2)],), [(1, 3), (2, 5), (6, 2), (7, 0)]), (([],), []), (([(0, 2, 3), (2, 4, 3)],), [(0, 3), (4, 0)]), (([(0, 4, 5), (1, 3, 2)],), [(0, 5), (4, 0)])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(1, 4, 3), (2, 6, 5), (6, 7, 2)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
