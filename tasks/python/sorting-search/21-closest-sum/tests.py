import pytest
from solution import closest_three as solve

@pytest.mark.parametrize('args, expected', [(([-1, 2, 1, -4], 1), 2), (([0, 0, 0], 1), 0), (([0, 1, 3, 4], 6), 5), (([1, 1, 1, 1], 4), 3)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([-1, 2, 1, -4], 1)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_inputs_against_triples():
    from itertools import combinations
    import random
    rng=random.Random(18)
    for _ in range(100):
        values=[rng.randint(-8,8) for _ in range(rng.randint(3,9))]; target=rng.randint(-10,10)
        expected=min(map(sum,combinations(values,3)),key=lambda s:(abs(s-target),s))
        assert solve(values,target)==expected
