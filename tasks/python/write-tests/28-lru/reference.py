from solution import LRU

def test_get_refreshes_recency():
    c = LRU(2)
    c.put('a', 0)
    c.put('b', 2)
    assert c.get('a') == 0
    c.put('c', 3)
    assert c.get('b') is None
    assert c.get('a') == 0

def test_overwrite_refreshes_without_extra_slot():
    c = LRU(2)
    c.put('a', 1)
    c.put('b', 2)
    c.put('a', 10)
    c.put('c', 3)
    assert c.get('a') == 10
    assert c.get('b') is None
    assert c.get('c') == 3

def test_missing_read_does_not_evict():
    c = LRU(1)
    c.put('a', False)
    assert c.get('missing') is None
    assert c.get('a') is False

def test_zero_capacity_and_independent_instances():
    c = LRU(0)
    c.put('a', 1)
    assert c.get('a') is None
    a = LRU(1)
    b = LRU(1)
    a.put('x', 3)
    assert b.get('x') is None
