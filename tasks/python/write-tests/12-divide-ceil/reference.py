import pytest
from solution import batch_count as solve

@pytest.mark.parametrize('args, expected', [((10, 3), 4), ((9, 3), 3), ((0, 4), 0), ((1, 1), 1), ((1, 0), '!error'), ((-1, 2), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (10, 3)
    before = deepcopy(args)
    solve(*args)
    assert args == before
