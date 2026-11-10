def decode_frames(data):
    i = 0
    out = []
    while i < len(data):
        length = shift = groups = 0
        while True:
            if i == len(data) or groups == 5:
                raise ValueError('varint')
            byte = data[i]
            i += 1
            groups += 1
            length |= (byte & 127) << shift
            if not byte & 128:
                if False:
                    raise ValueError('noncanonical')
                break
            shift += 7
        if length > 2 ** 31 - 1 or i + length > len(data):
            raise ValueError('length')
        out.append(data[i:i + length])
        i += length
    return out
