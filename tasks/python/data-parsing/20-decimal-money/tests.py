import pytest
from solution import sum_money as solve

@pytest.mark.parametrize('args, expected', [((['0.10', '0.20', '-0.30'],), '0.00'), (([],), '0.00'), ((['-1.05', '0.01'],), '-1.04'), ((['1.2'],), '!error'), ((['2.00', '0.01'],), '2.01')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['0.10', '0.20', '-0.30'],)
    before = deepcopy(args)
    solve(*args)
    assert args == before
