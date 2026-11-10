from solution import LfuCache


def test_example():
    c = LfuCache(2)
    c.put("a", 1)
    assert c.get("a") == 1
    c.put("b", 2)
    c.put("c", 3)
    assert c.get("b") is None
    assert c.get("a") == 1
    assert c.get("c") == 3


def test_frequency_beats_recency():
    c = LfuCache(2)
    c.put("a", 1)
    c.get("a")
    c.put("b", 2)
    c.put("c", 3)
    assert c.get("a") == 1
    assert c.get("b") is None


def test_tie_evicts_least_recently_used():
    c = LfuCache(2)
    c.put(1, "one")
    c.put(2, "two")
    assert c.get(1) == "one"
    c.put(3, "three")
    assert c.get(2) is None
    assert c.get(3) == "three"
    c.put(4, "four")
    assert c.get(1) is None
    assert c.get(3) == "three"
    assert c.get(4) == "four"


def test_put_existing_counts_as_use_and_replaces():
    c = LfuCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 10)
    c.put("c", 3)
    assert c.get("b") is None
    assert c.get("a") == 10


def test_evicted_key_starts_over():
    c = LfuCache(1)
    c.put("a", 1)
    c.get("a")
    c.get("a")
    c.put("b", 2)
    c.put("a", 3)
    c.put("c", 4)
    assert c.get("a") is None
    assert c.get("c") == 4


def test_missing_get_does_not_count():
    c = LfuCache(2)
    c.put("a", 1)
    assert c.get("zzz") is None
    c.put("b", 2)
    c.put("c", 3)
    assert c.get("a") is None


def test_zero_capacity():
    c = LfuCache(0)
    c.put("a", 1)
    assert c.get("a") is None


def test_many_operations():
    c = LfuCache(20_000)
    for i in range(100_000):
        c.put(i, i)
    assert c.get(0) is None
    assert c.get(99_999) == 99_999
    assert c.get(80_000) == 80_000
    assert c.get(79_999) is None
