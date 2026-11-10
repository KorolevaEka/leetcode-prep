from solution import TtlCache


def test_example():
    cache = TtlCache(10)
    cache.set("token", "abc", now=100)
    assert cache.get("token", now=109) == "abc"
    assert cache.get("token", now=110) is None
    assert cache.get("other", now=0) is None


def test_alive_just_before_expiry():
    cache = TtlCache(5)
    cache.set("k", 1, 0)
    assert cache.get("k", 4.5) == 1
    assert cache.get("k", 5) is None


def test_overwrite_restarts_ttl():
    cache = TtlCache(10)
    cache.set("k", "old", 0)
    cache.set("k", "new", 8)
    assert cache.get("k", 12) == "new"
    assert cache.get("k", 17) == "new"
    assert cache.get("k", 18) is None


def test_overwrite_after_expiry():
    cache = TtlCache(10)
    cache.set("k", "old", 0)
    assert cache.get("k", 20) is None
    cache.set("k", "new", 20)
    assert cache.get("k", 25) == "new"


def test_read_does_not_extend():
    cache = TtlCache(10)
    cache.set("k", "v", 0)
    assert cache.get("k", 9) == "v"
    assert cache.get("k", 10) is None


def test_keys_are_independent():
    cache = TtlCache(10)
    cache.set("a", 1, 0)
    cache.set("b", 2, 5)
    assert cache.get("a", 10) is None
    assert cache.get("b", 10) == 2
    assert cache.get("b", 15) is None


def test_falsy_values_are_stored():
    cache = TtlCache(10)
    cache.set("zero", 0, 0)
    cache.set("empty", "", 0)
    assert cache.get("zero", 1) == 0
    assert cache.get("empty", 1) == ""
