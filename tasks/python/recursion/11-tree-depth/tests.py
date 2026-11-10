import pytest
from solution import suite_depth as solve

@pytest.mark.parametrize('args, expected', [(({'children': [{'children': []}, {'children': [{'children': []}]}]},), 3), ((None,), 0), (({'children': []},), 1), (({'children': [{'children': []}, {'children': []}]},), 2)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ({'children': [{'children': []}, {'children': [{'children': []}]}]},)
    before = deepcopy(args)
    solve(*args)
    assert args == before
