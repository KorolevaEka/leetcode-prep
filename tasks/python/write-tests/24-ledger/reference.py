import pytest
from solution import Ledger

def test_transfer_and_exact_retry():
    ledger = Ledger({'a': 10, 'b': 0})
    assert ledger.transfer('x', 'a', 'b', 10) is True
    assert ledger.transfer('x', 'a', 'b', 10) is False
    assert ledger.balance('a') == 0
    assert ledger.balance('b') == 10

def test_conflicting_retry():
    ledger = Ledger({'a': 10, 'b': 0})
    ledger.transfer('x', 'a', 'b', 2)
    with pytest.raises(ValueError):
        ledger.transfer('x', 'a', 'b', 3)
    assert ledger.balance('a') == 8

def test_failure_does_not_reserve_id_or_change_balances():
    ledger = Ledger({'a': 2, 'b': 0})
    with pytest.raises(ValueError):
        ledger.transfer('x', 'a', 'b', 3)
    assert ledger.balance('a') == 2
    assert ledger.balance('b') == 0
    assert ledger.transfer('x', 'a', 'b', 1) is True

def test_arguments_and_input_copy():
    initial = {'a': 4, 'b': 0}
    ledger = Ledger(initial)
    for source, target, amount in [('a', 'a', 1), ('a', 'b', 0), ('a', 'b', -1), ('a', 'missing', 1)]:
        with pytest.raises(ValueError):
            ledger.transfer('bad', source, target, amount)
    ledger.transfer('ok', 'a', 'b', 1)
    assert initial == {'a': 4, 'b': 0}
