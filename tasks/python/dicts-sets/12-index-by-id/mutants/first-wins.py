def index_by_id(items: list[dict]) -> dict:
    result: dict = {}
    for item in items:
        if "id" in item:
            result.setdefault(item["id"], item)
    return result
