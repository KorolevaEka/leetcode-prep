import pytest
from solution import queen_placements as solve

@pytest.mark.parametrize('args, expected', [((4,), [[1, 3, 0, 2], [2, 0, 3, 1]]), ((0,), [[]]), ((1,), [[0]]), ((2,), []), ((3,), [])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (4,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
