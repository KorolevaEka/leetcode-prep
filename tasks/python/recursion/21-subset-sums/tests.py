import pytest
from solution import subset_sums as solve

@pytest.mark.parametrize('args, expected', [(([1, 2, 2],), [0, 1, 2, 3, 4, 5]), (([],), [0]), (([-2, 3],), [-2, 0, 1, 3]), (([0, 0],), [0])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 2, 2],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
