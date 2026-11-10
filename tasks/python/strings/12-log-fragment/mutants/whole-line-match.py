def shortest_fragment(lines: list[str], keys: list[str]) -> list[str]:
    if not keys:
        return []
    hits = [[j for j, key in enumerate(keys) if key == line] for line in lines]
    counts = [0] * len(keys)
    covered = 0
    best = None
    left = 0
    for right, found in enumerate(hits):
        for j in found:
            counts[j] += 1
            if counts[j] == 1:
                covered += 1
        while covered == len(keys):
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)
            for j in hits[left]:
                counts[j] -= 1
                if counts[j] == 0:
                    covered -= 1
            left += 1
    return [] if best is None else lines[best[0]:best[1] + 1]
