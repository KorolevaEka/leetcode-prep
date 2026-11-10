import pytest
from solution import Scheduler

def test_claim_reserves_and_finish_unblocks():
    s = Scheduler({'b': ['a'], 'a': []})
    assert s.claim() == 'a'
    assert s.claim() is None
    s.finish('a', True)
    assert s.claim() == 'b'
    assert s.claim() is None

def test_failure_blocks_only_dependents():
    s = Scheduler({'a': [], 'b': ['a'], 'c': []})
    assert s.claim() == 'a'
    s.finish('a', False)
    assert s.claim() == 'c'
    s.finish('c', True)
    assert s.claim() is None

def test_requires_all_dependencies_and_lexical_order():
    s = Scheduler({'z': [], 'a': [], 'b': ['a', 'z']})
    assert s.claim() == 'a'
    s.finish('a', True)
    assert s.claim() == 'z'
    assert s.claim() is None
    s.finish('z', True)
    assert s.claim() == 'b'

def test_invalid_finish_and_cycles():
    s = Scheduler({'a': []})
    with pytest.raises(ValueError):
        s.finish('a', True)
    s.claim()
    s.finish('a', True)
    with pytest.raises(ValueError):
        s.finish('a', False)
    assert Scheduler({'a': ['b'], 'b': ['a']}).claim() is None
