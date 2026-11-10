import pytest
from solution import rounded_price as solve

@pytest.mark.parametrize('args, expected', [(('2.675',), '2.68'), (('-1.235',), '-1.24'), (('0.004',), '0.00'), (('-0.001',), '0.00'), (('1',), '1.00'), (('1.245',), '1.25')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ('2.675',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
