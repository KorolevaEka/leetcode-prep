def shortest_chunk(log: list[str], required: set[str]) -> int:
    counts: dict[str, int] = {}
    covered = 0
    best = -1
    left = 0
    for right, event in enumerate(log):
        if event in required:
            counts[event] = counts.get(event, 0) + 1
            if counts[event] == 1:
                covered += 1
        while required and covered == len(required):
            size = right - left + 1
            if best == -1 or size < best:
                best = size
            gone = log[left]
            if gone in required:
                counts[gone] -= 1
                if counts[gone] == 0:
                    covered -= 1
            left += 1
    return best
