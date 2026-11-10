def parse_query(qs: str) -> dict[str, str | list[str]]:
    if qs.startswith("?"):
        qs = qs[1:]
    result = {}
    for pair in qs.split("&"):
        key, _, value = pair.partition("=")
        if not key:
            continue
        result[key] = value
    return result
