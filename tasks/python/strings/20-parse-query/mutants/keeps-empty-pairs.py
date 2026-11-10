def parse_query(qs: str) -> dict[str, str | list[str]]:
    if qs.startswith("?"):
        qs = qs[1:]
    result = {}
    for pair in qs.split("&"):
        key, _, value = pair.partition("=")
        if key not in result:
            result[key] = value
        elif isinstance(result[key], list):
            result[key].append(value)
        else:
            result[key] = [result[key], value]
    return result
