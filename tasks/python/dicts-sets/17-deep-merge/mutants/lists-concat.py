def deep_merge(base: dict, override: dict) -> dict:
    result = dict(base)
    for key, value in override.items():
        old = result.get(key)
        if isinstance(old, dict) and isinstance(value, dict):
            result[key] = deep_merge(old, value)
        elif isinstance(old, list) and isinstance(value, list):
            result[key] = old + value
        else:
            result[key] = value
    return result
