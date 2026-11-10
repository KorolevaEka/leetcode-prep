import pytest
from solution import longest_uniform as solve

@pytest.mark.parametrize('args, expected', [((['A', 'A', 'B', 'A', 'B', 'B', 'A'], 1), 4), (([], 2), 0), ((['A', 'B', 'A', 'B'], 2), 4), ((['A', 'B', 'B', 'A'], 0), 2), ((['A', 'B', 'C', 'D', 'E'], 1), 2)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (['A', 'A', 'B', 'A', 'B', 'B', 'A'], 1)
    before = deepcopy(args)
    solve(*args)
    assert args == before

def test_last_status_need_not_be_the_most_frequent():
    assert solve(['A', 'A', 'B'], 1) == 3


def test_windows_against_replacement_definition():
    from itertools import product
    from collections import Counter
    for n in range(6):
        for values in product('ABC',repeat=n):
            for k in range(3):
                expected=0
                for i in range(n):
                    for j in range(i+1,n+1):
                        if j-i-max(Counter(values[i:j]).values())<=k: expected=max(expected,j-i)
                assert solve(list(values),k)==expected
