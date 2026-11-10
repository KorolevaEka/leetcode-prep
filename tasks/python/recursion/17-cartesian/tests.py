import pytest
from solution import parameter_matrix as solve

@pytest.mark.parametrize('args, expected', [(([[1, 2], ['a', 'b']],), [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]), (([],), [[]]), (([[], [1]],), []), (([[1]],), [[1]])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[1, 2], ['a', 'b']],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
