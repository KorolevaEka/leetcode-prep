def flatten(items: list) -> list[str]:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(reversed(flatten(item)))
        else:
            result.append(item)
    return result
