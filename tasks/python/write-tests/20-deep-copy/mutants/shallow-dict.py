def clone_json(value):
    if isinstance(value, dict):
        return dict(value)
    if isinstance(value, list):
        return [clone_json(v) for v in value]
    return value
