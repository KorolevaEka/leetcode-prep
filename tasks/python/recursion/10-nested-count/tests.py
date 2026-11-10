import pytest
from solution import measurement_count as solve

@pytest.mark.parametrize('args, expected', [(([[1, 2], [], [3, [4]]],), 4), (([],), 0), ((5,), 1), (([[], [[]]],), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[1, 2], [], [3, [4]]],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
