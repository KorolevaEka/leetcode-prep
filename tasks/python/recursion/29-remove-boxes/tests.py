import pytest
from solution import cleanup_score as solve

@pytest.mark.parametrize('args, expected', [(([1, 3, 2, 2, 2, 3, 4, 3, 1],), 23), (([],), 0), (([1, 1, 1],), 9), (([1, 2, 1],), 5), (([1, 2, 3],), 3)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3, 2, 2, 2, 3, 4, 3, 1],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
