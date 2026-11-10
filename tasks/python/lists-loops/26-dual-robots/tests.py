import pytest
from solution import collected_artifacts as solve

@pytest.mark.parametrize('args, expected', [(([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]],), 24), (([[4]],), 4), (([[1], [2], [3]],), 6), (([[1, 0, 2], [0, 9, 0]],), 12)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
