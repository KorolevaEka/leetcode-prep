def find_pair(durations: list[int], slot: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for j, d in enumerate(durations):
        i = seen.get(slot - d)
        if i is not None:
            return (i, j)
        seen[d] = j
    return None
