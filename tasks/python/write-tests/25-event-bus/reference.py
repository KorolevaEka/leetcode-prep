import pytest
from solution import EventBus

def test_order_and_independent_subscription_tokens():
    b = EventBus()
    seen = []
    callback = lambda x: seen.append(x)
    a = b.subscribe(callback)
    c = b.subscribe(callback)
    assert a != c
    b.publish(0)
    assert seen == [0, 0]
    assert b.unsubscribe(a) is True
    assert b.unsubscribe(a) is False
    b.publish(1)
    assert seen == [0, 0, 1]

def test_snapshot_with_remove_and_add():
    b = EventBus()
    seen = []
    added = []

    def first(value):
        seen.append(('first', value))
        b.unsubscribe(second)
        if not added:
            added.append(b.subscribe(lambda v: seen.append(('new', v))))
    b.subscribe(first)
    second = b.subscribe(lambda v: seen.append(('second', v)))
    b.publish(1)
    assert seen == [('first', 1), ('second', 1)]
    b.publish(2)
    assert seen[-2:] == [('first', 2), ('new', 2)]

def test_nested_publish_uses_current_subscriptions():
    b = EventBus()
    seen = []

    def callback(value):
        seen.append(('a', value))
        if value == 1:
            b.subscribe(lambda v: seen.append(('b', v)))
            b.publish(2)
    b.subscribe(callback)
    b.publish(1)
    assert seen == [('a', 1), ('a', 2), ('b', 2)]

def test_exceptions_stop_delivery():
    b = EventBus()
    seen = []

    def bad(value):
        raise ValueError('bad')
    b.subscribe(bad)
    b.subscribe(seen.append)
    with pytest.raises(ValueError):
        b.publish(1)
    assert seen == []
