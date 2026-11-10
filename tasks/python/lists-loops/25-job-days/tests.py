import pytest
from solution import min_day_cost as solve

@pytest.mark.parametrize('args, expected', [(([6, 5, 4, 3, 2, 1], 2), 7), (([9, 9], 3), -1), (([], 0), 0), (([1, 8, 2], 1), 8), (([1, 8, 2], 3), 11), (([2], 0), -1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([6, 5, 4, 3, 2, 1], 2)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_schedules_against_all_cuts():
    import random
    from itertools import combinations
    rng=random.Random(17)
    for _ in range(80):
        n=rng.randint(1,7); values=[rng.randint(1,9) for _ in range(n)]
        days=rng.randint(1,n)
        expected=float('inf')
        for cuts in combinations(range(1,n),days-1):
            bounds=(0,)+cuts+(n,)
            expected=min(expected,sum(max(values[a:b]) for a,b in zip(bounds,bounds[1:])))
        assert solve(values,days)==expected
