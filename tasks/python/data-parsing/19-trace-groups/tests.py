import pytest
from solution import trace_records as solve

@pytest.mark.parametrize('args, expected', [((['@ fail', '  frame', '', '@ pass'],), ['fail\n  frame\n', 'pass']), (([],), []), ((['orphan'],), '!error'), ((['@ ', ' body '],), ['\n body '])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['@ fail', '  frame', '', '@ pass'],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
