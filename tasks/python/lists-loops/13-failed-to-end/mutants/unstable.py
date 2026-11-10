def move_failed_last(results: list[dict]) -> None:
    i, j = 0, len(results) - 1
    while i < j:
        if results[i]["status"] == "failed":
            while j > i and results[j]["status"] == "failed":
                j -= 1
            results[i], results[j] = results[j], results[i]
            j -= 1
        i += 1
