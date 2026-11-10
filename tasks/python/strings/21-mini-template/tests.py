import pytest
from solution import render

NESTED = "{% if a %}A{% if b %}B{% else %}b{% endif %}{% else %}a{% endif %}"


@pytest.mark.parametrize("tpl, ctx, expected", [
    ("Hi{% if vip %}, VIP{% endif %}!", {"vip": True}, "Hi, VIP!"),
    ("Hi{% if vip %}, VIP{% endif %}!", {"vip": False}, "Hi!"),
    ("{% if a %}A{% else %}{{ n }}{% endif %}", {"n": 5}, "5"),
    ("{{ x }}-{{x}}-{{  y}}", {"x": 1, "y": "z"}, "1-1-z"),
    ("{{ nope }}|", {}, "|"),
    ("{% if not a %}no{% endif %}", {}, "no"),
    ("{% if not a %}no{% else %}yes{% endif %}", {"a": 1}, "yes"),
    ("{%if a%}x{%endif%}", {"a": 1}, "x"),
    (NESTED, {"a": True, "b": True}, "AB"),
    (NESTED, {"a": True, "b": False}, "Ab"),
    (NESTED, {"a": False, "b": True}, "a"),
    (NESTED, {"a": False, "b": False}, "a"),
    ("{% if n %}x{% endif %}{{ n }}", {"n": 0}, "0"),
    ("{% if l %}x{% else %}empty{% endif %}", {"l": []}, "empty"),
    ("line1\n{% if a %}\nline2\n{% endif %}\nend", {"a": 1}, "line1\n\nline2\n\nend"),
    ("{{ a }}", {"a": "{{ b }}", "b": "X"}, "{{ b }}"),
    ("{{ a b }} {% if x", {}, "{{ a b }} {% if x"),
    ("plain", {}, "plain"),
    ("", {}, ""),
])
def test_render(tpl, ctx, expected):
    assert render(tpl, ctx) == expected


@pytest.mark.parametrize("tpl", [
    "{% endif %}", "{% else %}", "{% if a %}x", "{% if a %}{% else %}{% else %}{% endif %}",
    "{% foo %}", "{% if %}x{% endif %}", "{% if a b %}x{% endif %}", "{% if not %}x{% endif %}",
    "{% if a %}{% endif %}{% endif %}", "{% if a %}{% bad %}{% endif %}",
])
def test_errors(tpl):
    with pytest.raises(ValueError):
        render(tpl, {"a": False})
