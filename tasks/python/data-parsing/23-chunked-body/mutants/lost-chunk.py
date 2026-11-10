def decode_chunked(data):
    i = 0
    out = b''
    while True:
        end = data.find(b'\r\n', i)
        if end < 0:
            raise ValueError('header')
        token = data[i:end]
        if not token or any((c not in b'0123456789abcdefABCDEF' for c in token)):
            raise ValueError('size')
        size = int(token, 16)
        i = end + 2
        if i + size + 2 > len(data) or data[i + size:i + size + 2] != b'\r\n':
            raise ValueError('body')
        out = data[i:i + size]
        i += size + 2
        if size == 0:
            if i != len(data):
                raise ValueError('tail')
            return out
