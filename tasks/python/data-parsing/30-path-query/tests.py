import pytest
from solution import select_json as solve

@pytest.mark.parametrize('args, expected', [(({'a': {'id': 1}, 'id': 2}, '**/id'), [(('a', 'id'), 1), (('id',), 2)]), (([{'x': 1}, {'x': 2}], '*/x'), [((0, 'x'), 1), ((1, 'x'), 2)]), (({'a': 1}, ''), [((), {'a': 1})]), (({'x': 1}, '**/**/x'), [(('x',), 1)]), (({'a': 1}, 'b'), [])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'a': {'id': 1}, 'id': 2}, '**/id')
    before = deepcopy(args)
    solve(*args)
    assert args == before
