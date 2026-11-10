def find_pair(durations: list[int], slot: int) -> tuple[int, int] | None:
    first: dict[int, int] = {}
    for j, d in enumerate(durations):
        if d and (slot - d) in first:
            return (first[slot - d], j)
        first.setdefault(d, j)
    return None
