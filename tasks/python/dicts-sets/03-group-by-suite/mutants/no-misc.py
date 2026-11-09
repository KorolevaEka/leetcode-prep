def group_by_suite(names: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for name in names:
        if "." in name:
            suite, test = name.split(".", 1)
            groups.setdefault(suite, []).append(test)
    return groups
