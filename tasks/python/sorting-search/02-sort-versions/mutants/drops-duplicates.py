def sort_versions(versions: list[str]) -> list[str]:
    return sorted(set(versions), key=lambda v: tuple(int(part) for part in v.split(".")))
