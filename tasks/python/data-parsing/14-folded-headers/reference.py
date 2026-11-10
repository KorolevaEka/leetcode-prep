def folded_headers(lines):
    out = {}
    last = None
    for line in lines:
        if not line:
            continue
        if line[0] in ' \t':
            if last is None:
                raise ValueError('orphan continuation')
            out[last][-1] += ' ' + line.strip()
        else:
            key, sep, value = line.partition(':')
            if not sep or not key.strip():
                raise ValueError('invalid header')
            last = key.strip().lower()
            out.setdefault(last, []).append(value.strip())
    return out
