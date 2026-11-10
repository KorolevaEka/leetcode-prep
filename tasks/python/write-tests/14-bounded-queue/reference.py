import pytest
from solution import Queue

def test_fifo():
    q = Queue(3)
    assert q.push(0) is True
    q.push(None)
    assert q.pop() == 0
    assert q.pop() is None
    assert len(q) == 0

def test_full_rejection_is_atomic():
    q = Queue(1)
    q.push('a')
    assert q.push('b') is False
    assert len(q) == 1
    assert q.pop() == 'a'

def test_capacity_is_reusable():
    q = Queue(1)
    q.push(1)
    q.pop()
    assert q.push(2) is True
    assert q.pop() == 2

def test_empty_and_zero_capacity():
    q = Queue(0)
    assert q.push(1) is False
    with pytest.raises(IndexError):
        q.pop()
