import pytest
from solution import is_mirror as solve

@pytest.mark.parametrize('args, expected', [((['a', 'b', 'a'],), True), (([],), True), ((['a'],), True), ((['a', 'b'],), False), ((['a', 'b', 'c', 'a'],), False)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['a', 'b', 'a'],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
