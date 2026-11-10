import pytest
from solution import retry

def test_retries_until_success_and_stops():
    calls = []

    def op():
        calls.append(1)
        if len(calls) < 2:
            raise ValueError('temporary')
        return False
    assert retry(op, 4) is False
    assert len(calls) == 2

def test_exhaustion_preserves_error():
    calls = []
    error = ValueError('last')

    def op():
        calls.append(1)
        raise error
    with pytest.raises(ValueError) as caught:
        retry(op, 3)
    assert caught.value is error
    assert len(calls) == 3

def test_other_error_is_not_retried():
    calls = []

    def op():
        calls.append(1)
        raise TypeError('bug')
    with pytest.raises(TypeError):
        retry(op, 5)
    assert len(calls) == 1

def test_invalid_attempts_do_not_call():
    calls = []
    with pytest.raises(ValueError):
        retry(lambda: calls.append(1), 0)
    assert calls == []
