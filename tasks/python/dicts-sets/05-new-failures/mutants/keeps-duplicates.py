def new_failures(previous: list[str], current: list[str]) -> list[str]:
    known = set(previous)
    return [name for name in current if name not in known]
