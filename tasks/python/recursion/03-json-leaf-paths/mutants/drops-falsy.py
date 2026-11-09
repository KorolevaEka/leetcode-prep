def leaf_paths(data: dict) -> list[str]:
    paths: list[str] = []

    def walk(value, path: str) -> None:
        if isinstance(value, dict) and value:
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else key)
        elif isinstance(value, list) and value:
            for i, child in enumerate(value):
                walk(child, f"{path}[{i}]")
        elif value:
            paths.append(path)

    for key, child in data.items():
        walk(child, key)
    return paths
