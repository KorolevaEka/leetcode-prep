def parse_line(line: str) -> dict[str, str]:
    date, clock, level, rest = line.split(" ", 3)
    source, message = rest.split(": ", 1)
    return {"time": date, "level": level.strip("[]"), "source": source, "message": message}
