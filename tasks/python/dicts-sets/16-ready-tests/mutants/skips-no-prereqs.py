def ready_tests(deps: dict[str, list[str]], done: list[str]) -> list[str]:
    finished = set(done)
    return [t for t, pre in deps.items() if t not in finished and pre and all(p in finished for p in pre)]
