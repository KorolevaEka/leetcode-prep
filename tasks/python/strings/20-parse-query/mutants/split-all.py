def parse_query(qs: str) -> dict[str, str | list[str]]:
    if qs.startswith("?"):
        qs = qs[1:]
    result = {}
    for pair in qs.split("&"):
        fields = pair.split("=")
        key, value = fields[0], (fields[1] if len(fields) > 1 else "")
        if not key:
            continue
        if key not in result:
            result[key] = value
        elif isinstance(result[key], list):
            result[key].append(value)
        else:
            result[key] = [result[key], value]
    return result
