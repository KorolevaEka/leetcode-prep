import pytest
from solution import initial_energy as solve

@pytest.mark.parametrize('args, expected', [(([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],), 7), (([[0]],), 1), (([[-5]],), 6), (([[5]],), 1), (([[1, -4, 2]],), 4)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
