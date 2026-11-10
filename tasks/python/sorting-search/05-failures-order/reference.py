def most_failing(tests: list[tuple[str, int]]) -> list[str]:
    return [name for name, _ in sorted(tests, key=lambda t: t[1], reverse=True)]
