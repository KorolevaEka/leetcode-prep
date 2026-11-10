import pytest
from solution import shortest_fragment

EXAMPLE = ["start", "noise", "login ok", "noise", "cart ok", "login ok", "pay ok"]


@pytest.mark.parametrize("lines, keys, expected", [
    (EXAMPLE, ["login", "cart", "pay"], ["cart ok", "login ok", "pay ok"]),
    (["a1", "b1"], ["c"], []),
    (["a1", "b1"], [], []),
    ([], ["a"], []),
    (["a b c"], ["a", "b", "c"], ["a b c"]),
    (["x1", "y1", "x2", "y2"], ["x", "y"], ["x1", "y1"]),
    (["login cart", "pay"], ["login", "cart", "pay"], ["login cart", "pay"]),
    (["k1", "n", "k1", "k2"], ["k1", "k2"], ["k1", "k2"]),
    (["LOGIN"], ["login"], []),
    (["a", "b", "a", "n", "n", "b"], ["a", "b"], ["a", "b"]),
    (["only a", "only b"], ["a", "b", "zzz"], []),
    (["ab"], ["a"], ["ab"]),
])
def test_fragment(lines, keys, expected):
    assert shortest_fragment(lines, keys) == expected


def test_many_lines():
    lines = [f"noise {i}" for i in range(60000)]
    lines[100] = "alpha"
    lines[44998] = "alpha"
    lines[7000] = "beta"
    lines[45000] = "beta"
    lines[44999] = "gamma"
    assert shortest_fragment(lines, ["alpha", "beta", "gamma"]) == lines[44998:45001]
