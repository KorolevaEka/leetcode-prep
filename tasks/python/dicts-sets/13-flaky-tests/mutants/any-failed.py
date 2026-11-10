def flaky_tests(runs: list[tuple[str, bool]]) -> list[str]:
    result = []
    for name, passed in runs:
        if not passed and name not in result:
            result.append(name)
    return result
