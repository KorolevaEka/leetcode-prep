import pytest
from solution import last_position as solve

@pytest.mark.parametrize('args, expected', [((['a', 'b', 'a'], 'a'), 2), (([], 'a'), -1), (([1, 2, 3], 2), 1), (([1, 2], 5), -1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['a', 'b', 'a'], 'a')
    before = deepcopy(args)
    solve(*args)
    assert args == before
