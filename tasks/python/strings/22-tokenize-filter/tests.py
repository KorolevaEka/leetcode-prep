import pytest
from solution import tokenize_filter


@pytest.mark.parametrize("expr, expected", [
    ("status == 'not ok' and retries>=3",
     ["status", "==", "'not ok'", "and", "retries", ">=", "3"]),
    ("(a<1)", ["(", "a", "<", "1", ")"]),
    ("", []),
    ("   \t\n", []),
    ("a<=b", ["a", "<=", "b"]),
    ("a=b", ["a", "=", "b"]),
    ("x!='y z'", ["x", "!=", "'y z'"]),
    ("'a b''c'", ["'a b'", "'c'"]),
    ("t>2.5", ["t", ">", "2.5"]),
    ("a >= 1 and (b < 2)", ["a", ">=", "1", "and", "(", "b", "<", "2", ")"]),
    ("name=''", ["name", "=", "''"]),
    ("x ==\n'a'", ["x", "==", "'a'"]),
])
def test_tokenize(expr, expected):
    assert tokenize_filter(expr) == expected


@pytest.mark.parametrize("expr", ["x == 'a", "'", "a ! b", "a @ b", 'a == "b"', "a & b"])
def test_errors(expr):
    with pytest.raises(ValueError):
        tokenize_filter(expr)
