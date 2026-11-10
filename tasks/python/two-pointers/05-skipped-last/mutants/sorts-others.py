def skipped_last(results: list[str]) -> list[str]:
    return sorted(r for r in results if r != "skipped") + [r for r in results if r == "skipped"]
