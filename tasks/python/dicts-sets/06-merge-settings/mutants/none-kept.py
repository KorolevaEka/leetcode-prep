def merge_settings(defaults: dict, overrides: dict) -> dict:
    result = dict(defaults)
    result.update(overrides)
    return result
