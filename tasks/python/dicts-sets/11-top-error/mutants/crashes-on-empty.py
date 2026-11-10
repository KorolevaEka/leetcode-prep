def top_error(errors: list[str]) -> str | None:
    counts: dict[str, int] = {}
    for error in errors:
        counts[error] = counts.get(error, 0) + 1
    best = next(iter(counts))
    for error, count in counts.items():
        if count > counts[best]:
            best = error
    return best
