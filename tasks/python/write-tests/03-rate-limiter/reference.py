import pytest
from solution import RateLimiter


def test_allows_up_to_limit():
    limiter = RateLimiter(limit=2, window=10)
    assert limiter.allow("a", 0) is True
    assert limiter.allow("a", 1) is True


def test_rejects_over_limit():
    limiter = RateLimiter(limit=2, window=10)
    limiter.allow("a", 0)
    limiter.allow("a", 1)
    assert limiter.allow("a", 2) is False


def test_single_slot_limit():
    limiter = RateLimiter(limit=1, window=10)
    assert limiter.allow("a", 0) is True
    assert limiter.allow("a", 1) is False


def test_request_leaves_window_exactly_at_boundary():
    limiter = RateLimiter(limit=1, window=10)
    assert limiter.allow("a", 0) is True
    assert limiter.allow("a", 9.9) is False
    assert limiter.allow("a", 10) is True


def test_keys_are_independent():
    limiter = RateLimiter(limit=1, window=10)
    assert limiter.allow("a", 0) is True
    assert limiter.allow("b", 0) is True
    assert limiter.allow("a", 1) is False


def test_rejected_requests_do_not_take_a_slot():
    limiter = RateLimiter(limit=2, window=10)
    assert limiter.allow("a", 0) is True
    assert limiter.allow("a", 1) is True
    assert limiter.allow("a", 5) is False
    assert limiter.allow("a", 10) is True


def test_window_slides():
    limiter = RateLimiter(limit=2, window=10)
    limiter.allow("a", 0)
    limiter.allow("a", 6)
    assert limiter.allow("a", 12) is True
    assert limiter.allow("a", 13) is False
