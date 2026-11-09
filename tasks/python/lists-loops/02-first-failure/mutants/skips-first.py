def first_failure(statuses: list[str]) -> int:
    for i in range(1, len(statuses)):
        if statuses[i] == "failed":
            return i
    return -1
