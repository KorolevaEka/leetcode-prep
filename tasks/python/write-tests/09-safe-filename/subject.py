def safe_filename(name):
    return ''.join(('_' if c in '/\\\x00' else c for c in name))
