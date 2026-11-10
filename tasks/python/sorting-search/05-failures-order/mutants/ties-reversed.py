def most_failing(tests):
    return [name for name, _ in reversed(sorted(tests, key=lambda t: t[1]))]
