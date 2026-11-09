def leaf_paths(data: dict) -> list[str]:
    paths: list[str] = []

    def walk(value, path: str) -> None:
        if isinstance(value, dict) and value:
            for key, child in value.items():
                walk(child, f"{path}.{key}")
        elif isinstance(value, list) and value:
            for i, child in enumerate(value):
                walk(child, f"{path}[{i}]")
        else:
            paths.append(path)

    walk(data, "")
    return paths
