import re

_GROUP = re.compile(r"\{([0-9]+)\.\.([0-9]+)\}")


def expand_pattern(p: str) -> list[str]:
    m = _GROUP.search(p)
    if m is None:
        return [p]
    start, end = int(m.group(1)), int(m.group(2))
    if start > end:
        return []
    width = len(m.group(1)) if m.group(1).startswith("0") else 0
    tails = expand_pattern(p[m.end():])
    result = []
    for n in range(start, end + 1):
        head = p[:m.start()] + str(n).zfill(width)
        for tail in tails:
            result.append(head + tail)
    return result
