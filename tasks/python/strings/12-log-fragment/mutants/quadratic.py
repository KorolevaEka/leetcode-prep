def shortest_fragment(lines: list[str], keys: list[str]) -> list[str]:
    if not keys:
        return []
    best = None
    for left in range(len(lines)):
        seen = set()
        for right in range(left, len(lines)):
            for key in keys:
                if key in lines[right]:
                    seen.add(key)
            if len(seen) == len(keys):
                if best is None or right - left < best[1] - best[0]:
                    best = (left, right)
                break
    return [] if best is None else lines[best[0]:best[1] + 1]
