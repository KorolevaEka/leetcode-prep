def flaky_tests(runs: list[tuple[str, bool]]) -> list[str]:
    outcomes: dict[str, set[bool]] = {}
    for name, passed in runs:
        outcomes.setdefault(name, set()).add(passed)
    return sorted(n for n, o in outcomes.items() if len(o) == 2)
