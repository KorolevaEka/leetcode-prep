import pytest
from solution import parse_port as solve

@pytest.mark.parametrize('args, expected', [((' 443 ',), 443), (('1',), 1), (('65535',), 65535), (('0',), '!error'), (('65536',), '!error'), (('+80',), '!error'), (('١',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' 443 ',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
