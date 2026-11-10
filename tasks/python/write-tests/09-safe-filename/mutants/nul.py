def safe_filename(name):
    return ''.join(('_' if c in '/\\' else c for c in name))
