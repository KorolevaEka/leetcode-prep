import pytest
from solution import xml_cases as solve

@pytest.mark.parametrize('args, expected', [(('<report><case name="a" status="fail"><message>x<b>y</b>z</message></case></report>',), [('a', 'fail', 'xyz')]), (('<report/>',), []), (('<report><case name="a"/></report>',), [('a', 'unknown', '')]), (('<report><case/></report>',), '!error'), (('<report>',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('<report><case name="a" status="fail"><message>x<b>y</b>z</message></case></report>',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
