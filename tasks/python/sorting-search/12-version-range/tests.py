import pytest
from solution import versions_between as solve

@pytest.mark.parametrize('args, expected', [((['1.2', '1.10', '1.2.0', '2'], '1.2', '1.10'), ['1.2', '1.2.0', '1.10']), (([], '1', '2'), []), ((['1', '1.0', '0.9'], '1', '1'), ['1', '1.0']), ((['3'], '1', '2'), [])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['1.2', '1.10', '1.2.0', '2'], '1.2', '1.10')
    before = deepcopy(args)
    solve(*args)
    assert args == before
