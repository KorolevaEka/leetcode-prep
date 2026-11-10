def split_batches(tests: list[str], size: int) -> list[list[str]]:
    return [tests[i:i + size + 1] for i in range(0, len(tests), size + 1)]
