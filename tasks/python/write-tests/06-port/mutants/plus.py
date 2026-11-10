def parse_port(text):
    s = text.strip().lstrip('+')
    if not s or any((c not in '0123456789' for c in s)):
        raise ValueError('digits')
    p = int(s)
    if not 1 <= p <= 65535:
        raise ValueError('range')
    return p
