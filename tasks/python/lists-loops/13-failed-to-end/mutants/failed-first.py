def move_failed_last(results: list[dict]) -> None:
    results[:] = [r for r in results if r["status"] == "failed"] + [r for r in results if r["status"] != "failed"]
