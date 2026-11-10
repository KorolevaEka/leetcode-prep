import pytest
from solution import csv_row as solve

@pytest.mark.parametrize('args, expected', [((['a,b', 'x"y', 'line\nnext'],), '"a,b","x""y","line\nnext"\r\n'), (([],), '\r\n'), (([''],), '""\r\n'), ((['', 'x'],), ',x\r\n'), ((['a\rb'],), '"a\rb"\r\n')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['a,b', 'x"y', 'line\nnext'],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
