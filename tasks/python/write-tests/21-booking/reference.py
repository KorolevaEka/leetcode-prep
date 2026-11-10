import pytest
from solution import Bookings

def test_overlap_and_touch():
    b = Bookings()
    assert b.book(1, 3) is True
    assert b.book(2, 4) is False
    assert b.book(3, 5) is True

def test_rejected_booking_is_not_stored():
    b = Bookings()
    b.book(1, 3)
    b.book(2, 5)
    assert b.book(3, 5) is True

def test_exact_cancel_and_reuse():
    b = Bookings()
    b.book(1, 4)
    assert b.cancel(1, 3) is False
    assert b.cancel(1, 4) is True
    assert b.cancel(1, 4) is False
    assert b.book(1, 4) is True

def test_invalid_intervals():
    with pytest.raises(ValueError):
        Bookings().book(2, 2)
    with pytest.raises(ValueError):
        Bookings().book(3, 1)
