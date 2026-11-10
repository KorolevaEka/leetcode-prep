def new_failures(previous: list[str], current: list[str]) -> list[str]:
    result = []
    for name in current:
        if name not in result:
            result.append(name)
    return result
