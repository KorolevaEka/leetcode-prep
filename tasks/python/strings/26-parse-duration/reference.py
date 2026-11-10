import re

_PART = re.compile(r" *([0-9]+)(ms|h|m|s)")


def parse_duration(s: str) -> int:
    pos = 0
    seen = {}
    while (m := _PART.match(s, pos)):
        unit = m.group(2)
        if unit in seen:
            raise ValueError(f"duplicate unit {unit}")
        seen[unit] = int(m.group(1))
        pos = m.end()
    if not seen or s[pos:].strip(" ") != "":
        raise ValueError(f"bad duration {s!r}")
    return seen.get("h", 0) * 3600 + seen.get("m", 0) * 60 + seen.get("s", 0) + seen.get("ms", 0) // 1000
