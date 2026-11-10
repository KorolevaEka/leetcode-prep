import pytest
from solution import parse_tlv as solve

@pytest.mark.parametrize('args, expected', [((b'\x01\x00\x02ab\x80\x00\x04\x02\x00\x01z',), [(1, b'ab'), (128, [(2, b'z')])]), ((b'',), []), ((b'\x80\x00\x00',), [(128, [])]), ((b'\x01\x00',), '!error'), ((b'\x01\x00\x02a',), '!error'), ((b'\x80\x00\x01x',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (b'\x01\x00\x02ab\x80\x00\x04\x02\x00\x01z',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
