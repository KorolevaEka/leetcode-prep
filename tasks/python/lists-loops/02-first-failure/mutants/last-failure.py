def first_failure(statuses: list[str]) -> int:
    result = -1
    for i, status in enumerate(statuses):
        if status == "failed":
            result = i
    return result
