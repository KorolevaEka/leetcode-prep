import pytest
from solution import VersionStore

def test_versions_and_conflict():
    s = VersionStore()
    assert s.read('x') == (None, 0)
    assert s.commit({'x': 0}, {'x': 0}) is True
    assert s.read('x') == (0, 1)
    assert s.commit({'x': 2}, {'x': 0}) is False
    assert s.read('x') == (0, 1)
    assert s.commit({'x': 3}, {'x': 1}) is True
    assert s.read('x') == (3, 2)

def test_all_or_nothing_and_read_only_expectation():
    s = VersionStore()
    s.commit({'a': 1}, {'a': 0})
    assert s.commit({'b': 2, 'a': 9}, {'b': 0, 'a': 0}) is False
    assert s.read('b') == (None, 0)
    assert s.read('a') == (1, 1)
    assert s.commit({'b': 2}, {'b': 0, 'a': 0}) is False
    assert s.read('b') == (None, 0)

def test_copies_on_read_and_write():
    s = VersionStore()
    value = {'x': [1]}
    s.commit({'a': value}, {'a': 0})
    value['x'].append(2)
    read, version = s.read('a')
    read['x'].append(3)
    assert s.read('a') == ({'x': [1]}, 1)

def test_missing_expectation_and_empty_commit():
    s = VersionStore()
    with pytest.raises(ValueError):
        s.commit({'a': 1}, {})
    assert s.read('a') == (None, 0)
    assert s.commit({}, {}) is True
