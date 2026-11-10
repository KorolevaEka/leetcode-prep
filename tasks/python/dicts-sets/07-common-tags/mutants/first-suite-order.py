def common_tags(suites: list[list[str]]) -> list[str]:
    if not suites:
        return []
    common = set(suites[0])
    for tags in suites[1:]:
        common &= set(tags)
    return [tag for tag in suites[0] if tag in common]
