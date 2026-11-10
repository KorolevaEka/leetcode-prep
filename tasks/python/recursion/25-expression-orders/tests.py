import pytest
from solution import expression_results as solve

@pytest.mark.parametrize('args, expected', [(('2*3-4*5',), [-34, -14, -10, -10, 10]), (('11',), [11]), (('2-1-1',), [0, 2]), (('1+1+1',), [3, 3])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('2*3-4*5',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
