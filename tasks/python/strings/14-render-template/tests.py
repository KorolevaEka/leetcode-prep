import pytest
from solution import render_template


@pytest.mark.parametrize("tpl, values, expected", [
    ("Run {{ id }} on {{env}}", {"id": "42", "env": "qa"}, "Run 42 on qa"),
    ("Hi {{ who }}", {}, "Hi {{ who }}"),
    ("{{a}}", {"a": "{{b}}", "b": "X"}, "{{b}}"),
    ("{{}} and {{ }}", {"": "x"}, "{{}} and {{ }}"),
    ("{{ a b }}", {"a": "1", "b": "2"}, "{{ a b }}"),
    ("{{x}}-{{x}}-{{ x }}", {"x": "7"}, "7-7-7"),
    ("no placeholders", {"a": "1"}, "no placeholders"),
    ("", {"a": "1"}, ""),
    ("{{a}} {{missing}}  {{   b}}", {"a": "1", "b": "2"}, "1 {{missing}}  2"),
    ("{{ a }}", {"a": ""}, ""),
])
def test_render_template(tpl, values, expected):
    assert render_template(tpl, values) == expected
