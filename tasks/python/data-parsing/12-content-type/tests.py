import pytest
from solution import content_type as solve

@pytest.mark.parametrize('args, expected', [(('Text/Plain; Charset=UTF-8',), ('text/plain', {'charset': 'UTF-8'})), (('application/json',), ('application/json', {})), (('x/a; a=1; a=2',), ('x/a', {'a': '2'})), ((' x/y ; token=a=b ',), ('x/y', {'token': 'a=b'}))])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('Text/Plain; Charset=UTF-8',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
