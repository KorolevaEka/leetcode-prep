def parse_tlv(data):

    def parse(block):
        i = 0
        out = []
        while i < len(block):
            if i + 3 > len(block):
                raise ValueError('header')
            tag = block[i]
            size = int.from_bytes(block[i + 1:i + 3], 'big')
            i += 3
            if i + size > len(block):
                raise ValueError('payload')
            payload = block[i:i + size]
            i += size
            out.append((tag, parse(payload) if tag & 128 else payload))
        return out
    return parse(data)
