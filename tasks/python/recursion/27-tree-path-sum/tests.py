import pytest
from solution import max_tree_path as solve

@pytest.mark.parametrize('args, expected', [(((-10, (9, None, None), (20, (15, None, None), (7, None, None))),), 42), ((None,), None), (((-3, None, None),), -3), (((1, (2, None, None), (3, None, None)),), 6)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ((-10, (9, None, None), (20, (15, None, None), (7, None, None))),)
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_branch_cannot_be_reused_upward():
    assert solve((1, (2, (3, None, None), (4, None, None)), (5, None, None))) == 12
