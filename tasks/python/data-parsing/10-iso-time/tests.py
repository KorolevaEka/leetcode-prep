import pytest
from solution import utc_seconds as solve

@pytest.mark.parametrize('args, expected', [(('1970-01-01T00:00:00Z',), 0), (('1970-01-01T00:00:01Z',), 1), (('1970-01-02T00:00:00Z',), 86400), (('1969-12-31T23:59:59Z',), -1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('1970-01-01T00:00:00Z',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
