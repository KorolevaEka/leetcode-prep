def content_type(header):
    parts = header.split(';')
    params = {}
    for part in parts[1:]:
        key, _, value = part.partition('=')
        params.setdefault(key.strip().lower(), value.strip())
    return (parts[0].strip().lower(), params)
