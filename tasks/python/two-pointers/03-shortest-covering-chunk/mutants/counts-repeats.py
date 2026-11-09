def shortest_chunk(log: list[str], required: set[str]) -> int:
    if not required:
        return 0
    best = -1
    for left in range(len(log)):
        found = 0
        for right in range(left, len(log)):
            if log[right] in required:
                found += 1
            if found >= len(required):
                size = right - left + 1
                if best == -1 or size < best:
                    best = size
                break
    return best
