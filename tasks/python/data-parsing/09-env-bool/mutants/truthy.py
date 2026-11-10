def parse_flag(text):
    x = text.strip().lower()
    if x in ('true', 'yes', '1'):
        return True
    if x in ('false', 'no', '0'):
        return True
    return None
