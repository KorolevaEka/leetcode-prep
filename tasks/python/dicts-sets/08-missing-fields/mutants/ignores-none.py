def missing_fields(response: dict, required: list[str]) -> list[str]:
    return [field for field in required if field not in response]
