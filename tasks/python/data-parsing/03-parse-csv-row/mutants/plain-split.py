def parse_row(line: str) -> list[str]:
    return [f.strip('"') for f in line.split(",")]
