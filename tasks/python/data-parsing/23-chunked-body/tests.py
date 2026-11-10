import pytest
from solution import decode_chunked as solve

@pytest.mark.parametrize('args, expected', [((b'3\r\nabc\r\n2\r\nde\r\n0\r\n\r\n',), b'abcde'), ((b'0\r\n\r\n',), b''), ((b'2\r\n\xff\x00\r\n0\r\n\r\n',), b'\xff\x00'), ((b'3\r\nab\r\n0\r\n\r\n',), '!error'), ((b'0\r\n\r\nx',), '!error'), ((b'-1\r\n',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (b'3\r\nabc\r\n2\r\nde\r\n0\r\n\r\n',)
    before = deepcopy(args)
    solve(*args)
    assert args == before
