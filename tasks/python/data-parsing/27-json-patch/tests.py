import pytest
from solution import apply_patch as solve

@pytest.mark.parametrize('args, expected', [(({'x': [1, 2]}, [{'op': 'add', 'path': ['x', 1], 'value': 9}, {'op': 'remove', 'path': ['x', 0]}]), {'x': [9, 2]}), (({}, []), {}), (([], [{'op': 'add', 'path': [0], 'value': 1}]), [1]), (({}, [{'op': 'replace', 'path': ['x'], 'value': 1}]), '!error'), (({'x': 1}, [{'op': 'replace', 'path': [], 'value': [3]}]), [3]), (([1], [{'op': 'remove', 'path': [-1]}]), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'x': [1, 2]}, [{'op': 'add', 'path': ['x', 1], 'value': 9}, {'op': 'remove', 'path': ['x', 0]}])
    before = deepcopy(args)
    solve(*args)
    assert args == before
