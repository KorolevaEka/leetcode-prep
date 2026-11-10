def common_tags(suites: list[list[str]]) -> list[str]:
    result: set[str] = set()
    for tags in suites:
        result |= set(tags)
    return sorted(result)
