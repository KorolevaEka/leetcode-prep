def find_pair(durations: list[int], slot: int) -> tuple[int, int] | None:
    first: dict[int, int] = {}
    for j, d in enumerate(durations):
        i = first.get(slot - d)
        if i is not None:
            return (i, j)
        first.setdefault(d, j)
    return None
