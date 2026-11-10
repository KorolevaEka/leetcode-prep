import pytest
from solution import paired_actions as solve

@pytest.mark.parametrize('args, expected', [((3,), ['((()))', '(()())', '(())()', '()(())', '()()()']), ((0,), ['']), ((1,), ['()']), ((2,), ['(())', '()()'])])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (3,)
    before = deepcopy(args)
    solve(*args)
    assert args == before
