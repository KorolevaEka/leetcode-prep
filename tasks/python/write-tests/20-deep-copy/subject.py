def clone_json(value):
    if isinstance(value, dict):
        return {k: clone_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clone_json(v) for v in value]
    return value
