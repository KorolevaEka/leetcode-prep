import pytest
from solution import find_suite_path as solve

@pytest.mark.parametrize('args, expected', [(({'name': 'root', 'children': [{'name': 'x', 'children': [{'name': 'a', 'children': []}]}]}, 'a'), ['root', 'x', 'a']), ((None, 'x'), None), (({'name': 'x', 'children': []}, 'x'), ['x']), (({'name': 'r', 'children': [{'name': 'x', 'children': []}, {'name': 'b', 'children': [{'name': 'x', 'children': []}]}]}, 'x'), ['r', 'x'])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'name': 'root', 'children': [{'name': 'x', 'children': [{'name': 'a', 'children': []}]}]}, 'a')
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_matching_internal_node():
    assert solve({'name': 'r', 'children': [{'name': 'x', 'children': []}]}, 'r') == ['r']
