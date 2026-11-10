import pytest
from solution import max_courses as solve

@pytest.mark.parametrize('args, expected', [(([(100, 200), (200, 1300), (1000, 1250), (2000, 3200)],), 3), (([],), 0), (([(3, 3)],), 1), (([(5, 5), (2, 6), (2, 6)],), 2), (([(4, 2)],), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(100, 200), (200, 1300), (1000, 1250), (2000, 3200)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
