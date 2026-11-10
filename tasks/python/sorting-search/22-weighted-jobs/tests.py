import pytest
from solution import best_reward as solve

@pytest.mark.parametrize('args, expected', [(([(1, 3, 5), (2, 4, 6), (3, 5, 5)],), 10), (([],), 0), (([(1, 2, 1), (2, 3, 1), (1, 3, 5)],), 5), (([(0, 1, 4), (1, 2, 5)],), 9)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([(1, 3, 5), (2, 4, 6), (3, 5, 5)],)
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_later_job_can_be_worse():
    assert solve([(0, 2, 100), (1, 3, 1)]) == 100


def test_small_jobs_against_all_subsets():
    import random
    from itertools import combinations
    rng=random.Random(19)
    for _ in range(80):
        jobs=[]
        for i in range(rng.randint(0,8)):
            start=rng.randint(-3,6); jobs.append((start,start+rng.randint(1,4),rng.randint(0,10)))
        expected=0
        for size in range(len(jobs)+1):
            for subset in combinations(jobs,size):
                ordered=sorted(subset)
                if all(a[1]<=b[0] for a,b in zip(ordered,ordered[1:])): expected=max(expected,sum(x[2] for x in subset))
        assert solve(jobs)==expected
