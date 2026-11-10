import pytest
from solution import prune_disabled as solve

@pytest.mark.parametrize('args, expected', [(({'name': 'r', 'enabled': True, 'children': [{'name': 'x', 'enabled': False, 'children': []}]},), {'name': 'r', 'enabled': True, 'children': []}), ((None,), None), (({'name': 'x', 'enabled': False, 'children': []},), None), (({'name': 'r', 'enabled': True, 'children': [{'name': 'a', 'enabled': True, 'children': []}]},), {'name': 'r', 'enabled': True, 'children': [{'name': 'a', 'enabled': True, 'children': []}]})])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'name': 'r', 'enabled': True, 'children': [{'name': 'x', 'enabled': False, 'children': []}]},)
    before = deepcopy(args)
    solve(*args)
    assert args == before
