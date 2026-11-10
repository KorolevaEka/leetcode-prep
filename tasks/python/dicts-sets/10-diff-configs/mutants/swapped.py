def diff_configs(old: dict, new: dict) -> dict[str, list[str]]:
    return {
        "added": sorted(old.keys() - new.keys()),
        "removed": sorted(new.keys() - old.keys()),
        "changed": sorted(k for k in old.keys() & new.keys() if old[k] != new[k]),
    }
