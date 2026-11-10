def new_failures(previous: list[str], current: list[str]) -> list[str]:
    known = set(previous)
    result = []
    for name in current:
        if name not in known and name not in result:
            result.append(name)
    return sorted(result)
