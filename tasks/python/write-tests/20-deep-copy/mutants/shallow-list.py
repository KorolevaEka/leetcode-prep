def clone_json(value):
    if isinstance(value, dict):
        return {k: clone_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return list(value)
    return value
