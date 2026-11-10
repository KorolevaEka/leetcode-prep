import pytest
from solution import mean_present as solve

@pytest.mark.parametrize('args, expected', [(([0, 10, None],), 5), (([None, None],), None), (([],), None), (([-2, 2],), 0), (([5],), 5)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([0, 10, None],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
