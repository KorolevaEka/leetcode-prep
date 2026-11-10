import pytest
from solution import byte_size as solve

@pytest.mark.parametrize('args, expected', [(('2 KiB',), 2048), (('0B',), 0), (('3MiB',), 3145728), ((' 7 B ',), 7)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('2 KiB',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
