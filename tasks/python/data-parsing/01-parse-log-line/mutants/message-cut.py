def parse_line(line: str) -> dict[str, str]:
    date, clock, level, rest = line.split(" ", 3)
    parts = rest.split(": ")
    return {"time": f"{date} {clock}", "level": level.strip("[]"), "source": parts[0], "message": parts[1]}
