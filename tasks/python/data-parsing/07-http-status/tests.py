import pytest
from solution import http_status as solve

@pytest.mark.parametrize('args, expected', [(('HTTP/1.1 404 Not Found',), (404, 'Not Found')), (('HTTP/2 204',), (204, '')), ((' HTTP/1.0 200 OK ',), (200, 'OK')), (('HTTP/1.1 500 Internal  Error',), (500, 'Internal  Error'))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('HTTP/1.1 404 Not Found',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
