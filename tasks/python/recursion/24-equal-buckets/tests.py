import pytest
from solution import equal_buckets as solve

@pytest.mark.parametrize('args, expected', [(([4, 3, 2, 3, 5, 2, 1], 4), True), (([1, 2, 3, 4], 3), False), (([], 1), False), (([2, 2, 2, 2, 3, 4, 5], 4), False), (([1, 1], 2), True)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([4, 3, 2, 3, 5, 2, 1], 4)
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_success_requires_backtracking():
    assert solve([2, 2, 2, 2, 3, 3], 2) is True
