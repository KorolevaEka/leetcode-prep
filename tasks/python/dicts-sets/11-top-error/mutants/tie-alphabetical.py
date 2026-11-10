def top_error(errors: list[str]) -> str | None:
    if not errors:
        return None
    counts: dict[str, int] = {}
    for error in errors:
        counts[error] = counts.get(error, 0) + 1
    return sorted(counts, key=lambda e: (-counts[e], e))[0]
