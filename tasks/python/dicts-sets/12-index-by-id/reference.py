def index_by_id(items: list[dict]) -> dict:
    return {item["id"]: item for item in items if "id" in item}
