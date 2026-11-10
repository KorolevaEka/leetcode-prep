import pytest
from solution import is_leap as solve

@pytest.mark.parametrize('args, expected', [((2024,), True), ((2023,), False), ((1900,), False), ((2000,), True)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (2024,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
