import pytest
from solution import rotated_index as solve

@pytest.mark.parametrize('args, expected', [(([4, 5, 6, 7, 0, 1, 2], 0), 4), (([], 3), -1), (([1], 1), 0), (([3, 1], 1), 1), (([1, 2, 3], 4), -1), (([4, 5, 1, 2, 3], 4), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([4, 5, 6, 7, 0, 1, 2], 0)
    before = deepcopy(args)
    solve(*args)
    assert args == before
