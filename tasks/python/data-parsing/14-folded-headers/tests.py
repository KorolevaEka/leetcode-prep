import pytest
from solution import folded_headers as solve

@pytest.mark.parametrize('args, expected', [((['X-A: first', ' next', 'x-a: second', '\tend'],), {'x-a': ['first next', 'second end']}), (([],), {}), (([' continuation'],), '!error'), ((['Location: a:b'],), {'location': ['a:b']})])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['X-A: first', ' next', 'x-a: second', '\tend'],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
