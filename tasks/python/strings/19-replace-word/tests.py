import pytest
from solution import replace_word


@pytest.mark.parametrize("text, old, new, expected", [
    ("valid_id id (id) ID", "id", "uid", "valid_id uid (uid) ID"),
    ("a.b axb a.bc", "a.b", "X", "X axb a.bc"),
    ("x id", "id", "\\n", "x \\n"),
    ("id", "id", "uid", "uid"),
    ("id.id,id", "id", "k", "k.k,k"),
    ("ids id_ _id", "id", "k", "ids id_ _id"),
    ("abc", "", "X", "abc"),
    ("", "id", "k", ""),
    ("call (id) now", "(id)", "[k]", "call [k] now"),
    ("id id", "id", "", " "),
    ("Id ID id", "id", "k", "Id ID k"),
])
def test_replace_word(text, old, new, expected):
    assert replace_word(text, old, new) == expected
