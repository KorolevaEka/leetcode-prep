from solution import VersionedConfig


def test_example():
    c = VersionedConfig()
    c.set("timeout", 5, 10)
    c.set("timeout", 8, 20)
    assert c.get("timeout", 15) == 5
    assert c.get("timeout", 20) == 8
    assert c.get("timeout", 9) is None


def test_unknown_key():
    c = VersionedConfig()
    assert c.get("x", 5) is None
    c.set("a", 1, 1)
    assert c.get("x", 5) is None


def test_query_in_the_past_after_later_writes():
    c = VersionedConfig()
    c.set("k", "v1", 1)
    c.set("k", "v2", 5)
    c.set("k", "v3", 9)
    assert c.get("k", 4) == "v1"
    assert c.get("k", 5) == "v2"
    assert c.get("k", 100) == "v3"
    assert c.get("k", 1) == "v1"
    assert c.get("k", 0) is None


def test_same_time_last_write_wins():
    c = VersionedConfig()
    c.set("k", "a", 5)
    c.set("k", "b", 5)
    assert c.get("k", 5) == "b"
    assert c.get("k", 6) == "b"


def test_delete_hides_value_until_next_set():
    c = VersionedConfig()
    c.set("k", 1, 1)
    c.delete("k", 4)
    assert c.get("k", 3) == 1
    assert c.get("k", 4) is None
    assert c.get("k", 7) is None
    c.set("k", 2, 8)
    assert c.get("k", 7) is None
    assert c.get("k", 8) == 2
    assert c.get("k", 3) == 1


def test_delete_and_set_same_time():
    c = VersionedConfig()
    c.set("k", 1, 3)
    c.delete("k", 6)
    c.set("k", 2, 6)
    assert c.get("k", 6) == 2
    c.delete("k", 6)
    assert c.get("k", 6) is None


def test_falsy_values():
    c = VersionedConfig()
    c.set("a", 0, 1)
    c.set("b", "", 1)
    c.set("c", False, 1)
    assert c.get("a", 1) == 0
    assert c.get("b", 1) == ""
    assert c.get("c", 1) is False


def test_keys_are_independent():
    c = VersionedConfig()
    c.set("a", 1, 1)
    c.set("b", 2, 2)
    c.delete("a", 3)
    assert c.get("b", 3) == 2
    assert c.get("a", 2) == 1


def test_many_writes():
    c = VersionedConfig()
    n = 100_000
    for t in range(n):
        c.set("k", t, t)
    for t in range(0, n, 1):
        assert c.get("k", t) == t
    assert c.get("k", -1) is None
