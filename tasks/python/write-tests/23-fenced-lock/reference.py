from solution import LeaseLock

def test_exclusion_and_boundary():
    lock = LeaseLock()
    token = lock.acquire('a', 0, 5)
    assert token is not None
    assert lock.acquire('a', 1, 5) is None
    assert lock.acquire('b', 4, 5) is None
    newer = lock.acquire('b', 5, 5)
    assert newer > token

def test_stale_token_cannot_release_new_lease():
    lock = LeaseLock()
    old = lock.acquire('a', 0, 1)
    new = lock.acquire('a', 1, 5)
    assert lock.release('a', old, 2) is False
    assert lock.acquire('b', 2, 1) is None
    assert lock.release('a', new, 2) is True

def test_owner_and_expiration_checked():
    lock = LeaseLock()
    token = lock.acquire('a', 0, 2)
    assert lock.release('b', token, 1) is False
    assert lock.release('a', token, 2) is False

def test_release_does_not_reuse_token():
    lock = LeaseLock()
    old = lock.acquire('a', 0, 5)
    assert lock.release('a', old, 1) is True
    assert lock.release('a', old, 1) is False
    assert lock.acquire('b', 1, 5) > old
