import pytest
from solution import merge_streams as solve

@pytest.mark.parametrize('args, expected', [(([[1, 4], [1, 3], [], [2]],), [1, 1, 2, 3, 4]), (([],), []), (([[], []],), []), (([[-3, 0], [-2, 0]],), [-3, -2, 0, 0])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[1, 4], [1, 3], [], [2]],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
