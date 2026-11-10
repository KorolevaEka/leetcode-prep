import pytest
from solution import nearest_k as solve

@pytest.mark.parametrize('args, expected', [(([1, 2, 3, 4, 5], 3, 4), [1, 2, 3, 4]), (([], 0, 0), []), (([1, 1, 2], 1, 2), [1, 1]), (([1, 3, 5], 9, 2), [3, 5]), (([1, 3], 2, 1), [1])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 2, 3, 4, 5], 3, 4)
    before = deepcopy(args)
    solve(*args)
    assert args == before
