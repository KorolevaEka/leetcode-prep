from solution import Cache

def test_expiration_boundary():
    c = Cache()
    c.put('a', 0, 10, 5)
    assert c.get('a', 14) == 0
    assert c.get('a', 15) is None

def test_zero_ttl_and_missing():
    c = Cache()
    assert c.get('x', 0) is None
    c.put('x', 1, 0, 0)
    assert c.get('x', 0) is None

def test_overwrite_resets_value_and_deadline():
    c = Cache()
    c.put('x', 1, 0, 2)
    c.put('x', 2, 1, 10)
    assert c.get('x', 3) == 2
    assert c.get('x', 11) is None

def test_keys_and_instances_are_independent():
    a = Cache()
    b = Cache()
    a.put('x', False, 0, 3)
    a.put('y', 7, 0, 9)
    assert a.get('x', 1) is False
    assert a.get('y', 5) == 7
    assert b.get('x', 1) is None
