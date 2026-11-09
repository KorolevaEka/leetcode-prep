def slugify(title: str) -> str:
    return "".join(ch if ch.isalnum() else "-" for ch in title.lower()).strip("-")
