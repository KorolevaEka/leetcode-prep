def parse_line(line: str) -> dict[str, str]:
    date, clock, level, rest = line.split(" ", 3)
    source, message = rest.split(": ", 1)
    return {"time": f"{date} {clock}", "level": level, "source": source, "message": message}
