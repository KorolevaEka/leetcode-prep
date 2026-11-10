import pytest
from solution import eval_formula


@pytest.mark.parametrize("expr, variables, expected", [
    ("1+2*3", {}, 7),
    ("(1+2)*3", {}, 9),
    ("10-3-2", {}, 5),
    ("100/10/5", {}, 2),
    ("-7/2", {}, -3),
    ("7/-2", {}, -3),
    ("-7/-2", {}, 3),
    ("8/3", {}, 2),
    ("0/-5", {}, 0),
    ("2*-3", {}, -6),
    ("-(1+2)*2", {}, -6),
    ("--3", {}, 3),
    ("  4  ", {}, 4),
    ("0", {}, 0),
    ("2-3", {}, -1),
    ("2--3", {}, 5),
    ("retries*2 + (base-1)*3", {"retries": 3, "base": 4}, 15),
    ("a_1+_b", {"a_1": 5, "_b": 6}, 11),
    ("\t1\t+\t2", {}, 3),
    ("((7))", {}, 7),
])
def test_eval(expr, variables, expected):
    assert eval_formula(expr, variables) == expected


@pytest.mark.parametrize("expr", ["", "   ", "1+", "(1", "1 2", ")", "()", "1/0", "x+1", "1+*2", "2 $ 3", "1)", "5/(3-3)"])
def test_errors(expr):
    with pytest.raises(ValueError):
        eval_formula(expr, {})
