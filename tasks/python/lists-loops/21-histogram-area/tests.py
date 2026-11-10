import pytest
from solution import largest_block as solve

@pytest.mark.parametrize('args, expected', [(([2, 1, 5, 6, 2, 3],), 10), (([],), 0), (([4],), 4), (([2, 2, 2],), 6), (([1, 2, 3],), 4), (([0, 3, 0],), 3)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([2, 1, 5, 6, 2, 3],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_histograms_against_rectangles():
    from itertools import product
    for n in range(5):
        for bars in product(range(3),repeat=n):
            expected=max((min(bars[i:j])*(j-i) for i in range(n) for j in range(i+1,n+1)),default=0)
            assert solve(list(bars))==expected


def test_large_flat_histogram():
    assert solve([3]*30000)==90000
