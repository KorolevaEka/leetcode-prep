def diff_configs(old: dict, new: dict) -> dict[str, list[str]]:
    return {
        "added": [k for k in new if k not in old],
        "removed": [k for k in old if k not in new],
        "changed": [k for k in old if k in new and old[k] != new[k]],
    }
