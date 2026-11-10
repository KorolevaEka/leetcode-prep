def new_failures(previous: list[str], current: list[str]) -> list[str]:
    known = set(previous)
    seen: set[str] = set()
    result = []
    for name in current:
        if name not in known and name not in seen:
            seen.add(name)
            result.append(name)
    return result
