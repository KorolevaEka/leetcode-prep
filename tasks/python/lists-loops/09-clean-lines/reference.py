def clean_lines(lines: list[str]) -> list[str]:
    stripped = (line.strip() for line in lines)
    return [line for line in stripped if line and not line.startswith("#")]
