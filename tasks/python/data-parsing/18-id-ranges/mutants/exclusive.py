import re

def parse_id_ranges(text):
    if not text.strip():
        return []
    out = set()
    for part in text.split(','):
        m = re.fullmatch('\\s*(\\d+)(?:-(\\d+))?\\s*', part)
        if not m:
            raise ValueError('range')
        a = int(m[1])
        b = int(m[2]) if m[2] is not None else a
        if a > b:
            raise ValueError('descending')
        out.update(range(a, b))
    return sorted(out)
