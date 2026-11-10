def flaky_tests(runs: list[tuple[str, bool]]) -> list[str]:
    first: dict[str, bool] = {}
    outcomes: dict[str, set[bool]] = {}
    for name, passed in runs:
        first.setdefault(name, passed)
        outcomes.setdefault(name, set()).add(passed)
    return [n for n, o in outcomes.items() if len(o) == 2 and first[n] is False]
