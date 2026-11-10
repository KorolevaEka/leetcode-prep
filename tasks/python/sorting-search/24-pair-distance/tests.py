import pytest
from solution import pair_distance as solve

@pytest.mark.parametrize('args, expected', [(([1, 3, 1], 1), 0), (([1, 6, 1], 3), 5), (([-3, -1, 4], 2), 5), (([1, 2, 3], 2), 1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3, 1], 1)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_distances_against_explicit_pairs():
    import random
    from itertools import combinations
    rng=random.Random(20)
    for _ in range(80):
        values=[rng.randint(-5,5) for _ in range(rng.randint(2,8))]
        expected=sorted(abs(a-b) for a,b in combinations(values,2))
        for k in (1,len(expected)//2+1,len(expected)):
            assert solve(values,k)==expected[k-1]


def test_many_different_values():
    assert solve(list(range(20000)),1)==1
