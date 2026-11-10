import pytest
from solution import offset_minutes as solve

@pytest.mark.parametrize('args, expected', [(('+02:30',), 150), (('-00:30',), -30), (('Z',), 0), (('+23:59',), 1439), (('+24:00',), '!error'), (('+01:60',), '!error'), (('2:30',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('+02:30',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
