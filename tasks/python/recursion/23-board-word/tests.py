import pytest
from solution import word_route as solve

@pytest.mark.parametrize('args, expected', [(([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'), True), (([['A', 'B']], 'ABA'), False), (([], ''), True), (([], 'A'), False), (([['A', 'X'], ['X', 'B']], 'AB'), False)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED')
    before = deepcopy(args)
    solve(*args)
    assert args == before
