import pytest
from solution import priority_order as solve

@pytest.mark.parametrize('args, expected', [(([4, 2, 3, 2, 1, 9], [2, 4]), [2, 2, 4, 1, 3, 9]), (([], []), []), (([3, 1, 3], []), [1, 3, 3]), (([5, 0, -1], [8, 5]), [5, -1, 0])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([4, 2, 3, 2, 1, 9], [2, 4])
    before = deepcopy(args)
    solve(*args)
    assert args == before
