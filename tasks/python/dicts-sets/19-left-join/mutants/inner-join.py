def left_join(left: list[dict], right: list[dict], key: str) -> list[dict]:
    index: dict = {}
    for row in right:
        if key in row:
            index.setdefault(row[key], []).append(row)
    result = []
    for row in left:
        if key in row:
            for match in index.get(row[key], []):
                result.append({**row, **match})
    return result
