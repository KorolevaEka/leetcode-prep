def clean_lines(lines: list[str]) -> list[str]:
    return [l for l in lines if l.strip() and not l.strip().startswith("#")]
