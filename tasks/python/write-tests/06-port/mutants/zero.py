def parse_port(text):
    s = text.strip()
    if not s or any((c not in '0123456789' for c in s)):
        raise ValueError('digits')
    p = int(s)
    if not 0 <= p <= 65535:
        raise ValueError('range')
    return p
