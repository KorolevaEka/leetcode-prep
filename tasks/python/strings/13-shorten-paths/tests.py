import pytest
from solution import shorten_paths


@pytest.mark.parametrize("paths, expected", [
    (["a/ui/x.png", "a/ui2/y.png"], ["ui/x.png", "ui2/y.png"]),
    (["/srv/run1/a.png"], ["a.png"]),
    (["a/x.png", "b/x.png"], ["a/x.png", "b/x.png"]),
    ([], []),
    (["/srv/a/1.png", "/srv/a/2.png"], ["1.png", "2.png"]),
    (["a/b/x.png", "a/x.png"], ["b/x.png", "x.png"]),
    (["x.png", "y.png"], ["x.png", "y.png"]),
    (["run/s/1.png", "run/s/1.png"], ["1.png", "1.png"]),
    (["/a/x", "/b/y"], ["a/x", "b/y"]),
    (["logs/ui/a/1.png", "logs/ui/b/2.png", "logs/ui/b/3.png"], ["a/1.png", "b/2.png", "b/3.png"]),
])
def test_shorten_paths(paths, expected):
    assert shorten_paths(paths) == expected
