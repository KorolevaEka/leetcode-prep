import pytest
from solution import mirror_tree as solve

@pytest.mark.parametrize('args, expected', [(((1, (2, None, (4, None, None)), (3, None, None)),), (1, (3, None, None), (2, (4, None, None), None))), ((None,), None), (((1, None, None),), (1, None, None)), (((1, (2, None, None), None),), (1, None, (2, None, None)))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ((1, (2, None, (4, None, None)), (3, None, None)),)
    before = deepcopy(args)
    solve(*args)
    assert args == before
