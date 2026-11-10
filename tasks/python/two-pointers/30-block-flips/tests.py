import pytest
from solution import min_resets as solve

@pytest.mark.parametrize('args, expected', [(([0, 1, 0], 1), 2), (([1, 1, 0], 2), -1), (([0, 0, 0, 1, 0, 1, 1, 0], 3), 3), (([], 2), 0), (([0, 0], 2), 1), (([1, 1], 3), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([0, 1, 0], 1)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_short_bitstrings_against_state_search():
    from itertools import product
    from collections import deque
    for n in range(6):
        for values in product((0,1),repeat=n):
            for k in range(1,n+2):
                queue=deque([(values,0)]); seen={values}; expected=-1
                while queue:
                    state,count=queue.popleft()
                    if all(state): expected=count; break
                    for start in range(n-k+1):
                        nxt=state[:start]+tuple(1-x for x in state[start:start+k])+state[start+k:]
                        if nxt not in seen: seen.add(nxt); queue.append((nxt,count+1))
                assert solve(list(values),k)==expected
