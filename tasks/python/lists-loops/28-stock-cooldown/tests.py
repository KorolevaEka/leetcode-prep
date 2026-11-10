import pytest
from solution import max_trade as solve

@pytest.mark.parametrize('args, expected', [(([1, 2, 3, 0, 2],), 3), (([],), 0), (([4],), 0), (([5, 4, 3],), 0), (([1, 4, 0, 5],), 5)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 2, 3, 0, 2],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_prices_against_action_enumeration():
    from itertools import product
    def brute(prices,i,holding,cooldown):
        if i==len(prices): return float('-inf') if holding else 0
        best=brute(prices,i+1,holding,False)
        if holding: best=max(best,prices[i]+brute(prices,i+1,False,True))
        elif not cooldown: best=max(best,-prices[i]+brute(prices,i+1,True,False))
        return best
    for n in range(6):
        for prices in product(range(3),repeat=n):
            assert solve(list(prices))==brute(prices,0,False,False)
