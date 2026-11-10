from solution import ReorderBuffer

def test_gap_then_flushes_all_ready():
    b = ReorderBuffer(1)
    assert b.push(3, 'c') == []
    assert b.push(2, 'b') == []
    assert b.push(1, 'a') == ['a', 'b', 'c']
    assert b.push(4, 'd') == ['d']

def test_pending_first_value_wins():
    b = ReorderBuffer(0)
    b.push(1, 'first')
    b.push(1, 'second')
    assert b.push(0, None) == [None, 'first']

def test_emitted_duplicate_ignored():
    b = ReorderBuffer(7)
    assert b.push(7, False) == [False]
    assert b.push(7, 'again') == []
    assert b.push(8, 0) == [0]

def test_instances_do_not_share_pending():
    a = ReorderBuffer(1)
    b = ReorderBuffer(1)
    a.push(2, 'x')
    assert b.push(1, 'b') == ['b']
    assert a.push(1, 'a') == ['a', 'x']
