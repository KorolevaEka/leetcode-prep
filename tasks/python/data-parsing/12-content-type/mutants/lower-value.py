def content_type(header):
    parts = header.split(';')
    params = {}
    for part in parts[1:]:
        key, _, value = part.partition('=')
        params[key.strip().lower()] = value.strip().lower()
    return (parts[0].strip().lower(), params)
