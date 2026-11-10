def missing_fields(response: dict, required: list[str]) -> list[str]:
    return sorted(field for field in required if response.get(field) is None)
