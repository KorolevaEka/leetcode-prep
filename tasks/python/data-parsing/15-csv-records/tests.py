import pytest
from solution import csv_records as solve

@pytest.mark.parametrize('args, expected', [(('id,note\n1,"a,b"\n2,"x\ny"',), [{'id': '1', 'note': 'a,b'}, {'id': '2', 'note': 'x\ny'}]), (('',), []), (('a,b\n1',), '!error'), (('a,a\n1,2',), '!error'), (('a\n""',), [{'a': ''}])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('id,note\n1,"a,b"\n2,"x\ny"',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
