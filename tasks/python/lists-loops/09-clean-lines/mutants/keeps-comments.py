def clean_lines(lines: list[str]) -> list[str]:
    return [l.strip() for l in lines if l.strip()]
