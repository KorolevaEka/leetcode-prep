import pytest
from solution import rolling_medians as solve

@pytest.mark.parametrize('args, expected', [(([1, 3, -1, -3, 5, 3, 6, 7], 3), [1, -1, -1, 3, 5, 6]), (([], 0), []), (([1, 4, 2, 3], 2), [2.5, 3, 2.5]), (([2, 2, 2], 1), [2, 2, 2]), (([-5, -1], 2), [-3])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3, -1, -3, 5, 3, 6, 7], 3)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_medians_against_sorted_windows():
    import random
    rng=random.Random(22)
    for _ in range(80):
        values=[rng.randint(-4,4) for _ in range(rng.randint(1,15))]
        for k in range(1,len(values)+1):
            expected=[]
            for start in range(len(values)-k+1):
                window=sorted(values[start:start+k]); expected.append((window[(k-1)//2]+window[k//2])/2)
            assert solve(values,k)==expected


def test_large_nontrivial_windows():
    values=[(i*7919)%10007 for i in range(50000)]
    result=solve(values,10001)
    assert len(result)==40000
    for i in (0,1,12345,39999):
        assert result[i]==sorted(values[i:i+10001])[5000]
