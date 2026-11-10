import pytest
from solution import TxStore


def test_example():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.set("a", 2)
    s.begin()
    s.delete("a")
    assert s.get("a") is None
    s.rollback()
    assert s.get("a") == 2
    s.commit()
    assert s.get("a") == 2


def test_plain_store_without_transactions():
    s = TxStore()
    assert s.get("x") is None
    s.set("x", 1)
    s.set("x", 2)
    assert s.get("x") == 2
    s.delete("x")
    s.delete("nothing")
    assert s.get("x") is None


def test_rollback_restores_value_and_removes_new_keys():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.set("a", 5)
    s.set("b", 7)
    s.rollback()
    assert s.get("a") == 1
    assert s.get("b") is None


def test_rollback_restores_deleted_key():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.delete("a")
    assert s.get("a") is None
    s.rollback()
    assert s.get("a") == 1


def test_commit_applies_changes_and_deletes():
    s = TxStore()
    s.set("a", 1)
    s.set("b", 2)
    s.begin()
    s.set("a", 10)
    s.delete("b")
    s.commit()
    assert s.get("a") == 10
    assert s.get("b") is None


def test_nested_commit_is_undone_by_outer_rollback():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.begin()
    s.set("a", 2)
    s.set("c", 3)
    s.commit()
    assert s.get("a") == 2
    s.rollback()
    assert s.get("a") == 1
    assert s.get("c") is None


def test_nested_commit_keeps_deletes_for_outer_commit():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.begin()
    s.delete("a")
    s.commit()
    assert s.get("a") is None
    s.commit()
    assert s.get("a") is None


def test_rollback_only_innermost():
    s = TxStore()
    s.begin()
    s.set("a", 1)
    s.begin()
    s.set("a", 2)
    s.rollback()
    assert s.get("a") == 1
    s.commit()
    assert s.get("a") == 1


def test_set_after_delete_in_same_transaction():
    s = TxStore()
    s.set("a", 1)
    s.begin()
    s.delete("a")
    s.set("a", 9)
    s.commit()
    assert s.get("a") == 9


def test_errors_without_transaction():
    s = TxStore()
    with pytest.raises(ValueError):
        s.commit()
    with pytest.raises(ValueError):
        s.rollback()
    s.begin()
    s.commit()
    with pytest.raises(ValueError):
        s.commit()


def test_deep_nesting():
    s = TxStore()
    s.set("base", 0)
    for i in range(500):
        s.begin()
        s.set(f"k{i}", i)
    assert s.get("k0") == 0 and s.get("k499") == 499 and s.get("base") == 0
    for _ in range(500):
        s.rollback()
    assert s.get("k0") is None and s.get("base") == 0
