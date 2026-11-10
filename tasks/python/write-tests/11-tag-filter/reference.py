import pytest
from solution import has_tag as solve

@pytest.mark.parametrize('args, expected', [(([' API ', 'UI'], 'api'), True), ((['payment'], 'pay'), False), (([], 'x'), False), ((['Straße'], 'STRASSE'), True), (([' '], ''), True)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([' API ', 'UI'], 'api')
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_unicode_casefold_on_wanted():
    assert solve(['STRASSE'], 'Straße') is True
