def slugify(title: str) -> str:
    parts = []
    current = []
    for ch in title.lower():
        if ch.isalnum():
            current.append(ch)
        elif current:
            parts.append("".join(current))
            current = []
    if current:
        parts.append("".join(current))
    return "-".join(parts)
