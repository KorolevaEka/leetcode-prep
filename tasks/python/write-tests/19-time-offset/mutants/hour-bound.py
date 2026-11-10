import re

def offset_minutes(text):
    if text == 'Z':
        return 0
    if not re.fullmatch('[+-][0-9]{2}:[0-9]{2}', text):
        raise ValueError('format')
    h, m = (int(text[1:3]), int(text[4:6]))
    if h > 24 or m > 59:
        raise ValueError('range')
    return (h * 60 + m) * (-1 if text[0] == '-' else 1)
