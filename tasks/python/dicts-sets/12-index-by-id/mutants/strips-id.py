def index_by_id(items: list[dict]) -> dict:
    return {item["id"]: {k: v for k, v in item.items() if k != "id"} for item in items if "id" in item}
