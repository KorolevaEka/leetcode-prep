def move_failed_last(results: list[dict]) -> None:
    rest = sorted((r for r in results if r["status"] != "failed"), key=lambda r: r["name"])
    results[:] = rest + [r for r in results if r["status"] == "failed"]
