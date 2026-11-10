def left_join(left: list[dict], right: list[dict], key: str) -> list[dict]:
    index: dict = {}
    for row in right:
        index.setdefault(row.get(key), []).append(row)
    result = []
    for row in left:
        matches = index.get(row.get(key), [])
        if matches:
            result.extend({**row, **m} for m in matches)
        else:
            result.append(dict(row))
    return result
