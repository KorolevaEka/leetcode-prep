def find_duplicates(users: list[dict]) -> list[list[int]]:
    groups: dict[str, list[int]] = {}
    for user in users:
        key = user["email"].strip().lower()
        groups.setdefault(key, []).append(user["id"])
    return [ids for ids in groups.values() if len(ids) > 1]
