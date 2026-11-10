import pytest
from solution import decode_frames as solve

@pytest.mark.parametrize('args, expected', [((b'\x03abc\x00\x01z',), [b'abc', b'', b'z']), ((b'',), []), ((b'\x80\x01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',), [b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']), ((b'\x80\x00',), '!error'), ((b'\x02x',), '!error'), ((b'\x80',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (b'\x03abc\x00\x01z',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
