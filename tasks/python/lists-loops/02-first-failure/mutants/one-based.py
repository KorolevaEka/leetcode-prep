def first_failure(statuses: list[str]) -> int:
    for i, status in enumerate(statuses, start=1):
        if status == "failed":
            return i
    return -1
