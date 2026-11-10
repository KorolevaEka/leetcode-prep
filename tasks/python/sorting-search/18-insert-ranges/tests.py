import pytest
from solution import insert_window as solve

@pytest.mark.parametrize('args, expected', [(([(1, 3), (6, 9)], (2, 7)), [(1, 9)]), (([], (2, 3)), [(2, 3)]), (([(1, 2), (4, 5)], (2, 4)), [(1, 5)]), (([(5, 7)], (0, 1)), [(0, 1), (5, 7)]), (([(1, 4)], (2, 3)), [(1, 4)])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(1, 3), (6, 9)], (2, 7))
    before = deepcopy(args)
    solve(*args)
    assert args == before
