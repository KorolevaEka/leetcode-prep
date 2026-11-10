import pytest
from solution import tree_cameras as solve

@pytest.mark.parametrize('args, expected', [(((0, (0, None, None), (0, None, None)),), 1), ((None,), 0), (((0, None, None),), 1), (((0, (0, (0, (0, None, None), None), None), None),), 2)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ((0, (0, None, None), (0, None, None)),)
    before = deepcopy(args)
    solve(*args)
    assert args == before
