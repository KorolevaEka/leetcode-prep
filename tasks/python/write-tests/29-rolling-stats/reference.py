from solution import RollingStats

def test_empty_and_single():
    s = RollingStats(3)
    assert s.snapshot() is None
    s.add(0)
    assert s.snapshot() == (1, 0, 0, 0, 0)

def test_even_and_odd_medians():
    s = RollingStats(4)
    for x in [9, 1, 3]:
        s.add(x)
    assert s.snapshot() == (3, 1, 9, 13 / 3, 3)
    s.add(7)
    assert s.snapshot() == (4, 1, 9, 5, 5)

def test_expiration_of_extrema_and_duplicates():
    s = RollingStats(3)
    for x in [9, 1, 1, 2]:
        s.add(x)
    assert s.snapshot() == (3, 1, 2, 4 / 3, 1)
    s.add(3)
    assert s.snapshot() == (3, 1, 3, 2, 2)

def test_capacity_one_and_read_is_stable():
    s = RollingStats(1)
    s.add(-4)
    s.add(2)
    assert s.snapshot() == (1, 2, 2, 2, 2)
    assert s.snapshot() == (1, 2, 2, 2, 2)
