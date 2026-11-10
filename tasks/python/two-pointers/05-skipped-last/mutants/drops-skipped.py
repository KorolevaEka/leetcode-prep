def skipped_last(results: list[str]) -> list[str]:
    return [r for r in results if r != "skipped"]
