def left_join(left: list[dict], right: list[dict], key: str) -> list[dict]:
    index: dict = {}
    for row in right:
        if key in row:
            index.setdefault(row[key], []).append(row)
    result = []
    for row in left:
        matches = index.get(row[key], []) if key in row else []
        if matches:
            result.extend({**m, **row} for m in matches)
        else:
            result.append(dict(row))
    return result
