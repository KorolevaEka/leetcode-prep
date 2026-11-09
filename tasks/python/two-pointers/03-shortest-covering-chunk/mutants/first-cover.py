def shortest_chunk(log: list[str], required: set[str]) -> int:
    if not required:
        return 0
    counts: dict[str, int] = {}
    covered = 0
    left = 0
    for right, event in enumerate(log):
        if event in required:
            counts[event] = counts.get(event, 0) + 1
            if counts[event] == 1:
                covered += 1
        if covered == len(required):
            while log[left] not in required or counts[log[left]] > 1:
                if log[left] in required:
                    counts[log[left]] -= 1
                left += 1
            return right - left + 1
    return -1
