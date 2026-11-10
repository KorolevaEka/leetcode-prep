import pytest
from solution import Breaker

def fail():
    raise ValueError('network')

def test_threshold_blocks_without_calling():
    b = Breaker(2, 10)
    with pytest.raises(ValueError):
        b.call(fail, 0)
    with pytest.raises(ValueError):
        b.call(fail, 1)
    seen = []
    with pytest.raises(RuntimeError):
        b.call(lambda: seen.append(1), 5)
    assert seen == []

def test_success_resets_consecutive_count():
    b = Breaker(2, 10)
    with pytest.raises(ValueError):
        b.call(fail, 0)
    assert b.call(lambda: False, 1) is False
    with pytest.raises(ValueError):
        b.call(fail, 2)
    assert b.call(lambda: 7, 3) == 7

def test_boundary_probe_recovers():
    b = Breaker(1, 10)
    with pytest.raises(ValueError):
        b.call(fail, 0)
    assert b.call(lambda: None, 10) is None
    assert b.call(lambda: 3, 11) == 3

def test_failed_probe_reopens_full_window():
    b = Breaker(1, 10)
    with pytest.raises(ValueError):
        b.call(fail, 0)
    with pytest.raises(ValueError):
        b.call(fail, 10)
    with pytest.raises(RuntimeError):
        b.call(lambda: 1, 19)
    assert b.call(lambda: 2, 20) == 2
