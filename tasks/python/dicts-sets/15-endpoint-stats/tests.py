import pytest
from solution import endpoint_stats


@pytest.mark.parametrize("calls, expected", [
    ([("/login", 120), ("/cart", 80), ("/login", 40), ("/login", 200)],
     {"/login": {"count": 3, "min": 40, "max": 200, "total": 360},
      "/cart": {"count": 1, "min": 80, "max": 80, "total": 80}}),
    ([], {}),
    ([("/a", 5)], {"/a": {"count": 1, "min": 5, "max": 5, "total": 5}}),
    ([("/a", 9), ("/a", 3), ("/a", 6)], {"/a": {"count": 3, "min": 3, "max": 9, "total": 18}}),
    ([("/a", 1), ("/a", 2), ("/a", 3)], {"/a": {"count": 3, "min": 1, "max": 3, "total": 6}}),
    ([("/a", 7), ("/b", 7), ("/a", 7)],
     {"/a": {"count": 2, "min": 7, "max": 7, "total": 14}, "/b": {"count": 1, "min": 7, "max": 7, "total": 7}}),
    ([("/z", 0), ("/z", 4)], {"/z": {"count": 2, "min": 0, "max": 4, "total": 4}}),
])
def test_endpoint_stats(calls, expected):
    assert endpoint_stats(calls) == expected
