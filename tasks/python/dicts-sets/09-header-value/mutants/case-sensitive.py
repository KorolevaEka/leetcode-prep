def header_value(headers: dict[str, str], name: str) -> str | None:
    return headers.get(name)
