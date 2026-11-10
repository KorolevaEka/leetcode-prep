import pytest
from solution import effective_settings as solve

@pytest.mark.parametrize('args, expected', [(({'name': 'r', 'settings': {'a': 1}, 'children': [{'name': 'x', 'settings': {'a': 0}, 'children': []}]}, {'b': 2}), [('r', {'b': 2, 'a': 1}), ('x', {'b': 2, 'a': 0})]), ((None, {}), []), (({'name': 'r', 'settings': {}, 'children': []}, {'x': 3}), [('r', {'x': 3})]), (({'name': 'r', 'settings': {'a': 1}, 'children': [{'name': 'x', 'settings': {'b': 2}, 'children': []}, {'name': 'y', 'settings': {}, 'children': []}]}, {}), [('r', {'a': 1}), ('x', {'a': 1, 'b': 2}), ('y', {'a': 1})])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'name': 'r', 'settings': {'a': 1}, 'children': [{'name': 'x', 'settings': {'a': 0}, 'children': []}]}, {'b': 2})
    before = deepcopy(args)
    solve(*args)
    assert args == before
