def humanize_status(code: str) -> str:
    s = code.replace("_", " ")
    return s[:1].upper() + s[1:]
