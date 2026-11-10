def common_tags(suites: list[list[str]]) -> list[str]:
    common = set(suites[0])
    for tags in suites[1:]:
        common &= set(tags)
    return sorted(common)
