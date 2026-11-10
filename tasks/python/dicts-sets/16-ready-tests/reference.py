def ready_tests(deps: dict[str, list[str]], done: list[str]) -> list[str]:
    finished = set(done)
    return [name for name, pre in deps.items() if name not in finished and finished.issuperset(pre)]
