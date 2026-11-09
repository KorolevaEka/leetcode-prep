def first_failure(statuses: list[str]) -> int:
    for i, status in enumerate(statuses):
        if status == "failed":
            return i
    return -1
