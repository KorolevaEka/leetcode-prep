def merge_settings(defaults: dict, overrides: dict) -> dict:
    for key, value in overrides.items():
        if value is None:
            defaults.pop(key, None)
        else:
            defaults[key] = value
    return defaults
