def top_error(errors: list[str]) -> str | None:
    counts: dict[str, int] = {}
    for error in errors:
        counts[error] = counts.get(error, 0) + 1
    best = None
    for error, count in counts.items():
        if best is None or count > counts[best]:
            best = error
    return best
