import pytest
from solution import window_peaks as solve

@pytest.mark.parametrize('args, expected', [(([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]), (([], 0), []), (([4, 4, 1], 2), [4, 4]), (([3, 1, 2], 1), [3, 1, 2]), (([-5, -2, -3], 3), [-2])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3, -1, -3, 5, 3, 6, 7], 3)
    before = deepcopy(args)
    solve(*args)
    assert args == before
