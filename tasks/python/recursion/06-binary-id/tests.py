import pytest
from solution import binary_id as solve

@pytest.mark.parametrize('args, expected', [((0,), '0'), ((1,), '1'), ((6,), '110'), ((13,), '1101')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (0,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
