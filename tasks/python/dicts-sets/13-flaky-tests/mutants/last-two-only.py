def flaky_tests(runs: list[tuple[str, bool]]) -> list[str]:
    history: dict[str, list[bool]] = {}
    for name, passed in runs:
        history.setdefault(name, []).append(passed)
    return [n for n, h in history.items() if len(h) >= 2 and h[-1] != h[-2]]
