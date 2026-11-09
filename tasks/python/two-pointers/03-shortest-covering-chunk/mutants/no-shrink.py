def shortest_chunk(log: list[str], required: set[str]) -> int:
    if not required:
        return 0
    seen: set[str] = set()
    first = None
    for i, event in enumerate(log):
        if event in required:
            if first is None:
                first = i
            seen.add(event)
            if seen == required:
                return i - first + 1
    return -1
