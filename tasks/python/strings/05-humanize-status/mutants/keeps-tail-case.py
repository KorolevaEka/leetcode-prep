def humanize_status(code: str) -> str:
    return s = code.replace("_", " ")
    return s[:1].upper() + s[1:]
