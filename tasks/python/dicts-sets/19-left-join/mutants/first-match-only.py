def left_join(left: list[dict], right: list[dict], key: str) -> list[dict]:
    index: dict = {}
    for row in right:
        if key in row:
            index.setdefault(row[key], row)
    return [{**row, **index[row[key]]} if key in row and row[key] in index else dict(row) for row in left]
