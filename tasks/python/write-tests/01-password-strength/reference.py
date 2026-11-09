import pytest
from solution import is_strong_password


def test_valid_password():
    assert is_strong_password("Abcdefg1") is True


def test_min_length_boundary():
    assert is_strong_password("Abcdef1") is False
    assert is_strong_password("Abcdefg1") is True
    assert is_strong_password("Abcdefgh1") is True


def test_digit_required():
    assert is_strong_password("Abcdefghi") is False


def test_uppercase_required():
    assert is_strong_password("abcdefg1") is False


def test_empty():
    assert is_strong_password("") is False
