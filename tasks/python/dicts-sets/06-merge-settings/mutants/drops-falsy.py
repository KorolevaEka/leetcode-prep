def merge_settings(defaults: dict, overrides: dict) -> dict:
    result = dict(defaults)
    for key, value in overrides.items():
        if not value:
            result.pop(key, None)
        else:
            result[key] = value
    return result
