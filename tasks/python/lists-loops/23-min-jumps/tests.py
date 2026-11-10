import pytest
from solution import min_jumps as solve

@pytest.mark.parametrize('args, expected', [(([2, 3, 1, 1, 4],), 2), (([3, 2, 1, 0, 4],), -1), (([],), 0), (([0],), 0), (([1, 1, 1],), 2), (([0, 2],), -1)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([2, 3, 1, 1, 4],)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_small_routes_against_breadth_first_search():
    from itertools import product
    from collections import deque
    for n in range(1,6):
        for reach in product(range(3),repeat=n):
            queue=deque([(0,0)]); seen={0}; expected=-1
            while queue:
                position,steps=queue.popleft()
                if position==n-1: expected=steps; break
                for nxt in range(position+1,min(n,position+reach[position]+1)):
                    if nxt not in seen: seen.add(nxt); queue.append((nxt,steps+1))
            assert solve(list(reach))==expected
