def flatten(items: list) -> list[str]:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item:
            result.append(item)
    return result
