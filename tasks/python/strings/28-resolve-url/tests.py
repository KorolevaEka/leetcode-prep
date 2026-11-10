import pytest
from solution import resolve_url

BASE = "https://qa.example.com/app/v1/page.html?x=1#top"


@pytest.mark.parametrize("ref, expected", [
    ("../img/a.png", "https://qa.example.com/app/img/a.png"),
    ("x.html", "https://qa.example.com/app/v1/x.html"),
    ("/login", "https://qa.example.com/login"),
    ("?q=2", "https://qa.example.com/app/v1/page.html?q=2"),
    ("http://other.io/z?a=1", "http://other.io/z?a=1"),
    ("../../../../x", "https://qa.example.com/x"),
    ("..", "https://qa.example.com/app/"),
    (".", "https://qa.example.com/app/v1/"),
    ("./a/./b", "https://qa.example.com/app/v1/a/b"),
    ("#sec", "https://qa.example.com/app/v1/page.html#sec"),
    ("", "https://qa.example.com/app/v1/page.html"),
    ("a.png?v=1#z", "https://qa.example.com/app/v1/a.png?v=1#z"),
    ("/a/../b/./c", "https://qa.example.com/b/c"),
])
def test_resolve(ref, expected):
    assert resolve_url(BASE, ref) == expected


@pytest.mark.parametrize("base, ref, expected", [
    ("https://h.io", "x", "https://h.io/x"),
    ("http://h.io:8080/a/b/", "c", "http://h.io:8080/a/b/c"),
    ("https://h.io/a/b.html", "../..", "https://h.io/"),
    ("https://h.io/a/", "../b/", "https://h.io/b/"),
])
def test_other_bases(base, ref, expected):
    assert resolve_url(base, ref) == expected
