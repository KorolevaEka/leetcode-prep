def humanize_status(code: str) -> str:
    return " ".join(p for p in code.split("_") if p).capitalize()
