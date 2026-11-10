import pytest
from solution import search_docs

DOCS = {"n1": "Login fails on Safari", "n2": "login ok, logs rotated", "n3": "safari login SLOW"}


@pytest.mark.parametrize("docs, query, expected", [
    (DOCS, "login safari", ["n1", "n3"]),
    (DOCS, "log", []),
    (DOCS, "   ", []),
    (DOCS, "", []),
    (DOCS, "LOGIN", ["n1", "n2", "n3"]),
    (DOCS, "safari safari login", ["n1", "n3"]),
    (DOCS, "login unknown", []),
    ({}, "a", []),
    ({"b": "x y", "a": "y x", "c": "x"}, "x y", ["a", "b"]),
    ({"d": "one\ttwo\nthree"}, "two three", ["d"]),
    ({"d": "ok,"}, "ok", []),
])
def test_search_docs(docs, query, expected):
    assert search_docs(docs, query) == expected
