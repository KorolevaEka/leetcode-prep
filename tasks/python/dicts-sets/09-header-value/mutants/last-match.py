def header_value(headers: dict[str, str], name: str) -> str | None:
    found = None
    for key, value in headers.items():
        if key.lower() == name.lower():
            found = value
    return found
